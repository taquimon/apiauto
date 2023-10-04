"""
(c) Copyright Jalasoft. 2023

rest_client.py
    wrapper from requests library
"""
import json
import logging

import requests

from config.config import TOKEN_TODO
from utils.logger import get_logger
from utils.singleton import Singleton

LOGGER = get_logger(__name__, logging.DEBUG)


class RestClient(metaclass=Singleton):
    """
    Class to define methods for RestClient wrapper
    """

    def send_request(self, method_name, session=None, url="", headers="", data=None):
        response_dict = {}
        methods = {
            "get": session.get,
            "post": session.post,
            "delete": session.delete,
        }
        if method_name not in methods:
            raise AssertionError("Invalid method name")

        LOGGER.info("Method Name: %s", method_name)
        LOGGER.info("Endpoint (URL): %s", url)

        try:
            response = methods[method_name](url, headers=headers, data=data)
            response.raise_for_status()
            LOGGER.info("Status code: %s", response.status_code)
            if hasattr(response, "request"):
                LOGGER.debug("Request: %s", response.request.headers)
            LOGGER.info("Response: %s", response.text)
            if response.text:
                response_dict["body"] = json.loads(response.text)
            else:
                response_dict["body"] = {"msg": "No body content"}

            response_dict["headers"] = response.headers
            response_dict["status"] = response.status_code

        except requests.exceptions.HTTPError as http_error:
            LOGGER.error("HTTP error: %s", http_error)
            if response.text:
                response_dict["body"] = {"msg": response.text}
            # else:
            #     response_dict["body"] = {"msg": "No body content"}

            response_dict["headers"] = response.headers
            response_dict["status"] = response.status_code
        except requests.exceptions.RequestException as request_error:
            LOGGER.error("Request error: %s", request_error)

        return response_dict

    def get(self, session, url_base, headers):
        """

        :param url_base:
        :param headers:
        :return:
        """
        return self.send_request("get", session, url_base, headers=headers)

    def post(self, session, url_base, headers, data):
        """

        :param url_base:
        :param headers:
        :return:
        """
        return self.send_request("post", session, url_base, headers, data=data)

    def delete(self, session, url_base, headers):
        """

        :param url_base:
        :param headers:
        :return:
        """
        return self.send_request("delete", session, url_base, headers)


if __name__ == '__main__':

    token = TOKEN_TODO
    print(token)
    headers = {
        "Authorization": f"Bearer {token}"
    }
    RestClient().send_request("get", session=requests.Session(),
                             url="https://api.todoist.com/rest/v2/projects",
                             headers=headers)
