from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Pages.BasePage import Page
from Locator.Locators import RadioButtonPageLocator
from selenium.webdriver.support.ui import WebDriverWait

class RadioButtonPage(Page):

    def __init__(self, driver):
        self.locator = RadioButtonPageLocator()
        super().__init__(driver)  

        
    def click_radio_male(self):
        self.find_element(*self.locator.GENDER_RADIO_MALE).click()

    def click_radio_female(self):
        self.find_element(*self.locator.GENDER_RADIO_FEMALE).click()

    def get_result_text(self):
        return self.find_element(*self.locator.GENDER_RESULT).text

    def click_submit_button(self):
        self.find_element(*self.locator.GENDER_SUBMIT_BUTTON).click()


    def click_radio_group_male(self):
        self.find_element(*self.locator.RADIO_MALE).click()

    def click_radio_group_female(self):
        self.find_element(*self.locator.RADIO_FEMALE).click()

    def click_radio_age_0_5(self):
        self.find_element(*self.locator.RADIO_AGE_0_5).click()

    def click_radio_age_5_15(self):
        self.find_element(*self.locator.RADIO_AGE_5_15).click()

    def click_radio_age_15_50(self):
        self.find_element(*self.locator.RADIO_AGE_15_50).click()

    def click_radio_group_btn(self):
        self.find_element(*self.locator.RADIO_SUBMIT_BUTTON).click()

    def get_radio_group_result_text(self):
        return self.find_element(*self.locator.RADIO_RESULT).text

    