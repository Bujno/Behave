from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Pages.BasePage import Page
from Locator.Locators import TableFilterPageLocator
from selenium.webdriver.support.ui import WebDriverWait

class TableFilterPage(Page):

    def __init__(self, driver):
        self.locator = TableFilterPageLocator()
        super().__init__(driver)  

    def is_displayed_green_record(self):
        return self.find_element(*self.locator.GREEN_RECORD).is_displayed()

    def is_displayed_red_record(self):
        return self.find_element(*self.locator.RED_RECORD).is_displayed()

    def is_displayed_orange_record(self):
        return self.find_element(*self.locator.ORANGE_RECORD).is_displayed()

    def click_green_button(self):
        self.find_element(*self.locator.GREEN_BUTTON).click()

    def click_red_button(self):
        self.find_element(*self.locator.RED_BUTTON).click()

    def click_orange_button(self):
        self.find_element(*self.locator.ORANGE_BUTTON).click()

    def click_all_button(self):
        self.find_element(*self.locator.ALL_BUTTON).click()