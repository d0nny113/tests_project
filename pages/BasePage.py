from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_cond


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://b2c.passport.rt.ru'
        self.find_element = driver.find_element
        self.find_elements = driver.find_elements
        self.timeout = 10
        self.execute_script = driver.execute_script

    def open(self):
        return self.driver.get(self.url)

    def wait_until_displayed_element(self, locator: tuple) -> WebElement:
        return WebDriverWait(self, self.timeout).until(exp_cond.visibility_of_element_located(locator))

    def wait_until_clickable(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(exp_cond.element_to_be_clickable(locator))

    def wait_until_displayed_elements(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(exp_cond.visibility_of_all_elements_located(locator))

    def wait_until_element_is_present(self, locator: tuple) -> WebElement:
        return WebDriverWait(self, self.timeout).until(exp_cond.presence_of_element_located(locator))

    def wait_until_vis(self, element) -> WebElement:
        return WebDriverWait(self, self.timeout).until(exp_cond.visibility_of(element))
