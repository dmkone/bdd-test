from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class WebApp:

    def __init__(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def load_page(self, page):
        self.driver.navigate(page)

    def click_element(self, *locator):
        self.driver.instance.find_element(*locator).click()

    def find_element(self, *locator):
        element = self.driver.instance.find_element(*locator)
        return element

    def element_exists(self, *locator):
        exists = False
        try:
            self.wait_for_element(*locator)
            exists = True
        except NoSuchElementException:
            pass
        return exists

    def wait_for_element(self, locator):
        """Select an element by waiting for it to become visible"""
        wait = WebDriverWait(self.driver.instance, 10)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element

    def wait_for_clickable(self, locator):
        """Select an element by waiting for it to become visible"""
        wait = WebDriverWait(self.driver.instance, 10)
        element = wait.until(EC.element_to_be_clickable(locator))
        return element

    def wait_to_be_selected(self, locator):
        wait = WebDriverWait(self.driver.instance, 10)
        element = wait.until(EC.element_to_be_selected(locator))
        return element

    def wait_for_elements(self, locator):
        """Select an element by waiting for it to become visible"""
        wait = WebDriverWait(self.driver.instance, 10)
        elements = wait.until(EC.visibility_of_all_elements_located(locator))
        return elements

    def wait_for_loading(self, locator):
        wait = WebDriverWait(self.driver.instance, 10)
        wait.until(EC.invisibility_of_element_located(locator))

    def verify_title_is_displayed(self, title):
        assert title in self.driver.instance.title

    def close_website(self):
        self.driver.instance.close()
