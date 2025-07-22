import unittest
from selenium import webdriver
from pages.sortPage import SortPage

class SortTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
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
