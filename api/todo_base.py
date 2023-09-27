import requests

from config.config import HEADERS
from utils.rest_client import RestClient
from utils.singleton import Singleton


class TodoBase(metaclass=Singleton):

    def __init__(self):
        self.url_projects = "https://api.todoist.com/rest/v2/projects"
        self.url_sections = "https://api.todoist.com/rest/v2/sections"
        self.url_tasks = "https://api.todoist.com/rest/v2/tasks"
        self.session = requests.Session()

    def get_all_projects(self):
        """

        :return:
        """
        response = RestClient().send_request("get", session=self.session,
                                             url=self.url_projects, headers=HEADERS)
        if len(response.json()) == 0:
            raise AssertionError("No projects available")

        return response

    def get_all_sections(self):
        response = RestClient().send_request("get", session=self.session,
                                             url=self.url_sections, headers=HEADERS)
        if len(response.json()) == 0:
            raise AssertionError("No sections available")

        return response

    def get_all_tasks(self):
        response = RestClient().send_request("get", session=self.session,
                                             url=self.url_tasks, headers=HEADERS)
        if len(response.json()) == 0:
            raise AssertionError("No tasks available")

        return response
