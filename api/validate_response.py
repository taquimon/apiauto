import json
import logging

from config.config import ABS_PATH
from utils.logger import get_logger
from utils.singleton import Singleton

LOGGER = get_logger(__name__, logging.DEBUG)


class ValidateResponse(metaclass=Singleton):

    def validate_response(self, actual_response, method=None, expected_status_code=200, feature=None):
        print(actual_response)
        file_name = f"{ABS_PATH}/api/input_data/{feature}_{method}_{expected_status_code}.json"
        input_data = self.get_input_data_from_json(file_name)
        print(input_data)
        if 'body' in actual_response and actual_response["body"] is not None:
            # compare actual with input data
            self.validate_value(actual_response["status"], input_data["response"]["status"], field="status")
            self.validate_value(actual_response["headers"], input_data["response"]["headers"], field="headers")
            self.validate_value(actual_response["body"], input_data["response"]["body"], field="body")

    def validate_value(self, actual_value, expected_value, field):
        LOGGER.debug("Validating %s:", field)
        msg_error = f"Expecting '{expected_value}' but received '{actual_value}'"
        if "body" in field:
            # compare 2 jsons
            if isinstance(actual_value, list):
                assert self.compare_json(expected_value[0], actual_value[0]), msg_error
            else:
                assert self.compare_json(expected_value, actual_value), msg_error
        elif "headers" in field:
            # compare json is json
            assert expected_value.items() <= actual_value.items(), msg_error
        else:
            # compare equals
            assert actual_value == expected_value, msg_error

    @staticmethod
    def get_input_data_from_json(file_name):
        """

        :param file_name:
        :return:
        """
        LOGGER.debug("Reading file: %s", file_name)
        with open(file_name, encoding="utf8") as json_file:
            data = json.load(json_file)
        LOGGER.debug("Content of JSON file: %s", data)

        json_file.close()

        return data

    @staticmethod
    def compare_json(json1, json2):
        """
        Compare keys of 2 jsons
        :param json1:
        :param json2:
        :return: boolean
        """
        for key in json1.keys():
            if key in json2.keys():
                LOGGER.debug("Key '%s' found in Json2", key)
            else:
                LOGGER.debug("Key '%s' not found in Json2", key)
                return False
        return True
