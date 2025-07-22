import unittest
from selenium import webdriver
from pages.sortPage import SortPage
from selenium.webdriver.chrome.options import Options

class SortTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu") 

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.set_window_size(1920, 1080)
        cls.page = SortPage(cls.driver)

    def test_sorting(self):
        self.page.navigator()
        self.page.clicktitle()
        self.page.LastMovie()

    def test_species(self):
        self.page.navigator()
        self.page.selectMovieEmpire()
        self.page.listOfSpecies()

    def test_planets(self):
        self.page.navigator()
        self.page.selectMoviePhantom()
        self.page.listOfPlanets()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
