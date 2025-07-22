import unittest
from pages.basePage import BasePage
from locators.sortLocators import SortLocators 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SortPage(BasePage):

    def navigator(self):
        self.visit("http://localhost:3000")

    def clicktitle(self):
        self.click(SortLocators.TITLE)

    def LastMovie(self):
        rows  = self.listOfWebElements(SortLocators.movieRows)
        last_row = rows[-1]
        film_title = last_row.find_element(By.TAG_NAME, "a").text
        assert film_title == "The Phantom Menace", f"Expected 'The Phantom Menace', but got '{film_title}'"

    def selectMovieEmpire(self):
        self.click(SortLocators.SELECTEDMOVIEEmpire)
    
    def selectMoviePhantom(self):
        self.click(SortLocators.SELECTEDMOVIEPHANTOM)

    def listOfSpecies(self):
        elements = self.listOfWebElements(SortLocators.ListOfSpieces)
        spieces_to_find = "Wookie"
        spieces = [el.text for el in elements]
        assert spieces_to_find in spieces, f"Title '{spieces_to_find}' not found in list: {spieces}"

    def listOfPlanets(self):
        elements = self.listOfWebElements(SortLocators.ListOfPlanets)
        spieces_to_find = "Wookie"
        planets = [el.text for el in elements]
        assert spieces_to_find not in planets, f"Title '{spieces_to_find}' not found in list: {planets}"