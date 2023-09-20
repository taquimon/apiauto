import unittest
import requests
from nose2.tools import params

"""
Test for nose2
"""


class Projects(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Setup Class only executed one time
        """
        print("Setup Class")
        cls.token = "9463fd6e63c3ac3e06372045795ef48264968d2c"
        cls.headers = {
            "Authorization": "Bearer {}".format(cls.token)
        }
        cls.url_base = "https://api.todoist.com/rest/v2/projects"

        # create project to be used in tests
        body_project = {
            "name": "Project 0"
        }
        response = requests.post(cls.url_base, headers=cls.headers, data=body_project)

        cls.project_id = response.json()["id"]
        cls.project_id_update = ""
        cls.projects_list = []

    def test_get_all_projects(self):
        """
        Test get all projects
        """
        response = requests.get(self.url_base, headers=self.headers)
        assert response.status_code == 200

    @params("Project 2", "1111111", "!@$$@$!@$")
    def test_create_project(self, name_project):
        """
        Test for create project
        """
        body_project = {
            "name": name_project
        }
        response = requests.post(self.url_base, headers=self.headers, data=body_project)
        print(response.json())
        self.project_id_update = response.json()["id"]
        self.projects_list.append(self.project_id_update)
        assert response.status_code == 200

    def test_get_project(self):
        """
        Test get Project
        """
        url = f"{self.url_base}/{self.project_id}"
        response = requests.get(url, headers=self.headers)
        print(response.json())
        assert response.status_code == 200

    def test_delete_project(self):
        url = f"{self.url_base}/{self.project_id}"
        print(f"Test Delete: {self.project_id}")
        response = requests.delete(url, headers=self.headers)
        # validate project has been deleted
        assert response.status_code == 204

    def test_update_project(self):
        url = f"{self.url_base}/{self.project_id_update}"
        data_update = {
            "name": "Project 2",
            "color": "red"
        }
        response = requests.post(url, headers=self.headers, data=data_update)
        print(response.json())
        assert response.status_code == 200

    @classmethod
    def tearDownClass(cls):
        print("tearDown Class")
        # delete projects created
        for project in cls.projects_list:
            url = f"{cls.url_base}/{project}"
            requests.delete(url, headers=cls.headers)
            print(f"Deleting project: {project}")
