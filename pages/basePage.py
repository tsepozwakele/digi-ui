from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def visit(self, url: str):
        self.driver.get(url)

    def find(self, locator: tuple):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator: tuple):
        self.find(locator).click()

    def type(self, locator: tuple, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator: tuple):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_text(self, locator: tuple):
        return self.find(locator).text

    def wait_for_element(self, locator: tuple):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def current_url(self):
        return self.driver.current_url
    
    def listOfWebElements(self, locator: tuple):
        by, value = locator
        return self.driver.find_elements(by, value)