import unittest


class TestProject(unittest.TestCase):

    # fixture
    def setUp(self):
        print("Setup")

    def test_one(self):
        print("test one")

    def test_two(self):
        print("test two")

    def test_three(self):
        print("test three")

    # fixture
    def tearDown(self):
        print("tearDown")
