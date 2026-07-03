import unittest

from utils import filter_by_source

class TestUtils(unittest.TestCase):

    def test_filter_source(self):

        articles = [

            {
                "source": {"name": "BBC"}
            },

            {
                "source": {"name": "CNN"}
            }

        ]

        result = filter_by_source(articles, "BBC")

        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()