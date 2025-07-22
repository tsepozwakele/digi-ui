from selenium.webdriver.common.by import By

class SortLocators:
    TITLE = (By.XPATH, "/html/body/section/main/table/thead/tr/th[1]")
    movieRows = (By.CSS_SELECTOR,"tbody tr")
    SELECTEDMOVIEEmpire = (By.XPATH, "//*[contains(text(), 'The Empire Strikes Back')]")
    SELECTEDMOVIEPHANTOM = (By.XPATH, "//*[contains(text(), 'The Phantom Menace')]")
    # ListOfSpieces = (By.XPATH, "//div/h1[contains(text(),'Species')]/following-sibling::ul/li")
    ListOfSpieces = (By.XPATH, "//div[h1='Species']/following-sibling::ul/li")
    ListOfPlanets = (By.XPATH, "//div[h1='Planets']/following-sibling::ul/li")
    # ListOfSpieces = (By.XPATH, "/html/body/section/main/div[2]/div[3]/div/h1")P