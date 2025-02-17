import unittest
from utils.twitter_api import get_twitter_api

class TestTwitterAPI(unittest.TestCase):
    def test_authentication(self):
        api = get_twitter_api()
        self.assertIsNotNone(api, "Twitter authentication failed")

if __name__ == "__main__":
    unittest.main()

