import logging
import unittest

import requests

from api.todo_base import TodoBase
from config.config import HEADERS
from utils.logger import get_logger
from utils.rest_client import RestClient

LOGGER = get_logger(__name__, logging.DEBUG)


class Tasks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url_tasks = "https://api.todoist.com/rest/v2/tasks"
        cls.session = requests.Session()

        cls.project_id = TodoBase().get_all_projects().json()[1]["id"]
        cls.section_id = TodoBase().get_all_sections().json()[1]["id"]
        cls.task_id = TodoBase().get_all_tasks().json()[1]["id"]
    def test_create_task(self):

        response = self.create_task()
        assert response.status_code == 200

    def test_create_task_with_project_id(self):
        project_id = self.project_id
        response = self.create_task(project_id=project_id)
        assert response.status_code == 200

    def test_create_task_with_section_id(self):
        section_id = self.section_id
        response = self.create_task(section_id=section_id)
        assert response.status_code == 200

    def test_get_all_tasks(self):

        response = TodoBase().get_all_tasks()
        LOGGER.info("Number of tasks returned: %s", len(response.json()))
        assert response.status_code == 200

    def test_get_task_by_id(self):
        task_id = self.task_id
        LOGGER.info("Task Id: %s", task_id)
        url_task = f"{self.url_tasks}/{task_id}"
        response = RestClient().send_request("get", session=self.session, headers=HEADERS, url=url_task)

        assert response.status_code == 200

    def test_close_task(self):

        task_id = self.task_id
        LOGGER.info("Task Id: %s", task_id)
        url_task_close = f"{self.url_tasks}/{task_id}/close"
        response = RestClient().send_request("post", session=self.session, headers=HEADERS,
                                             url=url_task_close)

        assert response.status_code == 204

    def test_reopen_task(self):
        # valid task open
        task_id = self.create_task().json()["id"]

        # close
        url_task_close = f"{self.url_tasks}/{task_id}/close"
        response_close = RestClient().send_request("post", session=self.session, headers=HEADERS,
                                                   url=url_task_close)

        assert response_close.status_code == 204

        LOGGER.info("Task Id: %s", task_id)
        url_task_reopen = f"{self.url_tasks}/{task_id}/reopen"
        response = RestClient().send_request("post", session=self.session, headers=HEADERS,
                                             url=url_task_reopen)

        assert response.status_code == 204

    def create_task(self, project_id=None, section_id=None):
        data = {
            "content": "Task inside section",
            "due_string": "tomorrow at 12:00",
            "due_lang": "en",
            "priority": 4
        }
        if project_id:
            data["project_id"] = project_id
        if section_id:
            data["section_id"] = section_id

        response = RestClient().send_request("post", session=self.session, headers=HEADERS,
                                             url=self.url_tasks, data=data)

        return response
