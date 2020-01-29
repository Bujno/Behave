from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Pages.BasePage import Page
from Locator.Locators import InputFormPageLocator
from selenium.webdriver.support.ui import WebDriverWait

class InputFormPage(Page):

    def __init__(self, driver):
        self.locator = InputFormPageLocator()
        super().__init__(driver)  

    def enter_message(self, value):
        self.find_element(*self.locator.MESSAGE_INPUT).clear()
        self.find_element(*self.locator.MESSAGE_INPUT).send_keys(value)

    def click_submit_button(self):
        self.find_element(*self.locator.MESSAGE_BUTTON).click()

    def get_message_result(self):
        return self.find_element(*self.locator.MESSAGE_RESULT).text
        
    def enter_a(self, value):
        self.find_element(*self.locator.INPUT_A).clear()
        self.find_element(*self.locator.INPUT_A).send_keys(value)

    def enter_b(self, value):
        self.find_element(*self.locator.INPUT_B).clear()
        self.find_element(*self.locator.INPUT_B).send_keys(value)

    def click_submit_ab_button(self):
        self.find_element(*self.locator.BUTTON).click()

    def get_ab_result(self):
        return self.find_element(*self.locator.RESULT).text

    