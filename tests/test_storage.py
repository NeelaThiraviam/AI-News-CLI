import unittest

from storage import save_articles
from storage import load_articles

class TestStorage(unittest.TestCase):

    def test_save_and_load(self):

        sample = [
            {
                "title": "OpenAI",
                "url": "https://example.com"
            }
        ]

        save_articles(sample)

        data = load_articles()

        self.assertEqual(data[0]["title"], "OpenAI")


if __name__ == "__main__":
    unittest.main()