"""
(c) Copyright Jalasoft. 2023

projects.py
    configuration of logger file
"""
import logging
import unittest
import requests
from nose2.tools import params

from config.config import TOKEN_TODO
from utils.logger import get_logger
from utils.rest_client import RestClient

LOGGER = get_logger(__name__, logging.DEBUG)


class Projects(unittest.TestCase):
    """
    Class for projects endpoint
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup Class only executed one time
        """
        print("Setup Class")
        cls.token = TOKEN_TODO

        print("Token from .env file: ", cls.token)
        cls.headers = {
            "Authorization": f"Bearer {cls.token}"
        }
        cls.url_base = "https://api.todoist.com/rest/v2/projects"

        # create project to be used in tests
        body_project = {
            "name": "Project 0"
        }
        response = requests.post(cls.url_base, headers=cls.headers, data=body_project)
        cls.rest_client = RestClient()
        cls.session = requests.Session()
        cls.project_id = response.json()["id"]
        cls.project_id_update = ""
        cls.projects_list = []

    def test_get_all_projects(self):
        """
        Test get all projects
        """
        response = self.rest_client.send_request("get", session=self.session,
                                                 url=self.url_base, headers=self.headers)
        assert response.status_code == 200

    @params("Project 2", "1111111", "!@$$@$!@$")
    def test_create_project(self, name_project):
        """
        Test for create project
        """
        body_project = {
            "name": name_project
        }
        response = self.rest_client.send_request("post", session=self.session, url=self.url_base,
                                                 headers=self.headers,
                                                 data=body_project)
        LOGGER.info("Response for create project: %s", response.json())
        self.project_id_update = response.json()["id"]
        LOGGER.debug("Project id generated: %s", self.project_id_update)
        self.projects_list.append(self.project_id_update)
        assert response.status_code == 200

    def test_get_project(self):
        """
        Test get Project
        """
        url = f"{self.url_base}/{self.project_id}"
        response = self.rest_client.send_request("get", session=self.session, url=url, headers=self.headers)
        print(response.json())
        assert response.status_code == 200

    def test_delete_project(self):
        """
        Test delete project
        :return:
        """
        url = f"{self.url_base}/{self.project_id}"
        print(f"Test Delete: {self.project_id}")
        response = self.rest_client.send_request("delete", session=self.session, url=url,
                                                 headers=self.headers)
        # validate project has been deleted
        assert response.status_code == 204

    def test_update_project(self):
        """
        Test update project
        :return:
        """
        url = f"{self.url_base}/{self.project_id_update}"
        data_update = {
            "name": "Project 2",
            "color": "red"
        }
        response = self.rest_client.send_request("post", session=self.session, url=url,
                                                 headers=self.headers, data=data_update)
        print(response.json())
        assert response.status_code == 200

    @classmethod
    def tearDownClass(cls):
        print("tearDown Class")
        # delete projects created
        for project in cls.projects_list:
            url = f"{cls.url_base}/{project}"
            cls.rest_client.send_request("delete", session=cls.session, url=url, headers=cls.headers)
            LOGGER.info("Deleting project: %s", {project})
