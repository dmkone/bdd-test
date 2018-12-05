from selenium import webdriver
from config import settings

class WebApp():

    instance = None

    def __init__(self):
        self.driver = webdriver.Chrome()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
            return cls.instance

    def load_website(self):
        self.driver.get(settings.base_url)

    def verify_title_is_displayed(self, title):
        assert title in self.driver.title

    def close_website(self):
        self.driver.quit()


webapp = WebApp.get_instance()