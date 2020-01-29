from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Pages.BasePage import Page
from Locator.Locators import AjaxFormPageLocators
from selenium.webdriver.support.ui import WebDriverWait

class AjaxFormPage(Page):

    def __init__(self, driver):
        self.locator = AjaxFormPageLocators
        super().__init__(driver)  

    def enter_text(self, value):
        self.find_element(*self.locator.TEXT).clear()
        self.find_element(*self.locator.TEXT).send_keys(value)

    def enter_name(self, value):
        self.find_element(*self.locator.NAME).clear()
        self.find_element(*self.locator.NAME).send_keys(value)

    def click_submit_button(self):
        self.find_element(*self.locator.BUTTON).click()

    def get_result(self):
        return self.find_element(*self.locator.RESULT).text
        

    