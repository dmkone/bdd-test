from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from framework.webapp import WebApp
import time


class AdDesignPageLocator(object):

    AD_DESIGN_TAB = (By.XPATH, "//a[contains(@href, 'addesign')]")
    CREATE_AD_DESIGN_BUTTON = (By.ID, "createAdDesignBtn")
    MODAL_ID = (By.ID, "createAdDesignModal")
    AD_ACCOUNT_OPTION = (By.XPATH, "//span[text()='Sandbox Adzwedo']")
    AD_ACCOUNT_DROPDOWN = (By.CLASS_NAME, "ad-account-select")
    PUBLISHED_POSTS_TABLE_ROW = (By.XPATH, "//div[@id='selectedByPublishedPosts']//tbody/tr")
    SELECT_BTN = (By.XPATH, "//div[@id='selectedByPublishedPosts']//tbody/tr//button")
    ERROR_LABEL = (By.CLASS_NAME, "error_message")
    LOADING_OVERLAY = (By.CLASS_NAME, "loading-overlay-popups")


class AdDesignPage(WebApp):

    def click_menu(self):
        element = self.wait_for_element(AdDesignPageLocator.AD_DESIGN_TAB)
        element.click()

    def verify_on_ad_design_page(self):
        element = self.wait_for_element(AdDesignPageLocator.CREATE_AD_DESIGN_BUTTON)
        assert element.is_displayed()

    def click_create_ad_design_button(self):
        self.click_element(*AdDesignPageLocator.CREATE_AD_DESIGN_BUTTON)

    def verify_ad_design_popup_is_displayed(self):
        element = self.wait_for_element(AdDesignPageLocator.MODAL_ID)
        assert element.get_attribute("aria-hidden") == "false"

    def select_ad_account(self):
        pass

    def click_box(self, box_name):
        box_locator = (By.XPATH, "//label[@for='{}']".format(box_name))
        self.wait_for_element(AdDesignPageLocator.AD_ACCOUNT_OPTION)
        box = self.wait_for_element(box_locator)
        box.click()

    def click_btn(self, btn_name):
        btn_locator = (By.XPATH, "//button[text()='{}']".format(btn_name))
        btn = self.wait_for_element(btn_locator)
        btn.click()

    def click_btn_popup(self, btn_name, ad_type):
        btn_locator = (By.XPATH, "//div[@id='{}']//button[text()='{}']".format(ad_type, btn_name))
        self.wait_for_loading(AdDesignPageLocator.LOADING_OVERLAY)
        btn = self.wait_for_element(btn_locator)
        btn.click()

    def screen_is_displayed(self, screen_name):
        screen = (By.XPATH, "//span[contains(text(), '{}')]".format(screen_name))
        element = self.wait_for_element(screen)
        assert element.is_displayed()

    def published_posts_exist(self):
        exist = self.element_exists(AdDesignPageLocator.PUBLISHED_POSTS_TABLE_ROW)
        assert exist

    def hover_and_click_on_post(self):
        action = ActionChains(self.driver.instance)
        row = self.wait_for_element(AdDesignPageLocator.PUBLISHED_POSTS_TABLE_ROW)
        action.move_to_element(row).perform()
        btn = self.wait_for_element(AdDesignPageLocator.SELECT_BTN)
        btn.click()

    def verify_ad_is_created(self, design_name):
        # TO DO
        # Please add a date check to make sure a new ad design has been created
        element_locator = (By.XPATH, "//h5[text()='{}']".format(design_name))
        element = self.element_exists(element_locator)
        assert element

    def verify_error_is_displayed(self, error_text):
        element = self.wait_for_element(AdDesignPageLocator.ERROR_LABEL)
        assert error_text == element.text

    def select_page(self, page):
        pass

    def click_on_pages(self):
        pass

    def fill_in_letters(self):
        selector = (By.XPATH, "//div[@class='bs-searchbox']/input")
        element = self.wait_for_element(selector)
        element.send_keys('Eff')

    def filter_pages(self):
        pass

    def select_ad_type(self, ad_type):
        selector = (By.XPATH, '//div[@class="filters-content--item"][3]')
        self.wait_for_element((By.CLASS_NAME, 'ads-block--content'))
        element = self.wait_for_clickable(selector)
        element.click()
        option_selector = (By.XPATH, '//li[text()="{}"]'.format(ad_type))
        option = self.wait_for_clickable(option_selector)
        option.click()

    def display_filtered_ad_designs(self, ad_type):
        selector = (By.XPATH, "//div[@class='ads-block']//h5")
        elements = self.wait_for_elements(selector)
        for element in elements:
            assert element.text == ad_type

    def select_date_range(self, date):
        selector = (By.XPATH, '//div[@class="filters-content--item"][4]')
        self.wait_for_element((By.CLASS_NAME, 'ads-block--content'))
        element = self.wait_for_clickable(selector)
        element.click()
        selector = (By.XPATH, '//li[text()="{}"]'.format(date))
        element = self.wait_for_clickable(selector)
        element.click()

    def enter_tag(self):
        pass

    def click_instagram_icon(self):
        pass

    def verify_ad_design_images_displayed(self):
        # TO DO
        # Please verify valid images are displayed
        pass

    def select_date_from_dropdown(self):
        pass

    def newest_to_oldest(self):
        # TO DO
        # To verify that ad designs are ordered from newest to oldest
        pass

    def adaccount_ad_desings(self):
        # TO DO
        # Please remove hard-coded values and change the XPATH selector
        selector = (By.XPATH, "//option[text()='Sandbox Adzwedo']")
        element = self.wait_for_element(selector)
        value = element.get_attribute('value')
        selector = (By.XPATH, "//div[@class='ads-block-content flex-content ad-items-flex-content addesign-list']/div")
        elements = self.wait_for_elements(selector)
        for element in elements:
            assert element.get_attribute('data-adaccountid') == value

    def page_ad_desings(self, pageid):
        # TO DO
        # Please change the XPATH selector
        selector = (By.XPATH, "//div[@class='ads-block-content flex-content ad-items-flex-content addesign-list']/div")
        elements = self.wait_for_elements(selector)
        for element in elements:
            assert element.get_attribute('data-pageid') == pageid