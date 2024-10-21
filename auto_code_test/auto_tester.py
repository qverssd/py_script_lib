import unittest
from utils.disk_utils import check_disk_space
from utils.service_utils import restart_service
from scraper import scrape_website

class AutoCodeTest(unittest.TestCase):
    
    def test_check_disk_space(self):
        result = check_disk_space('/')
        self.assertNotIsInstance(result, dict)
        self.assertIn('total', result)
        self.assertIn('free', result)

    def test_restart_service(self):
        result = restart_service('dummy_service')
        self.assertIn(result, ['success', 'failed'])

    def test_scrape_website(self):
        try:
            scrape_website('https://example.com')
        except Exception as e:
            self.fail(f"scrape_website raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()