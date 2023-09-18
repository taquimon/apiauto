import unittest
import requests

"""
Test for nose2
"""

class Projects(unittest.TestCase):

    def setUp(self):
        """
        Executed for each test
        :return:
        """
        print("setup")
        self.token = "9463fd6e63c3ac3e06372045795ef48264968d2c"
        self.headers = {
            "Authorization": "Bearer {}".format(self.token)
        }
        self.url_base = "https://api.todoist.com/rest/v2/projects"

    @classmethod
    def setUpClass(cls):
        """
        Setup Class only executed one time
        :return:
        """
        print("Setup Class")

    def test_one(self):
        print("Test one")

    def test_two(self):
        print("Test two")

    def tearDown(self):
        print("teardown")

    @classmethod
    def tearDownClass(cls):
        print("tearDown Class")
