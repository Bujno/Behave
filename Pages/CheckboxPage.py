from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Pages.BasePage import Page
from Locator.Locators import CheckBoxPageLocator
from selenium.webdriver.support.ui import WebDriverWait

class CheckboxPage(Page):

    def __init__(self, driver):
        self.locator = CheckBoxPageLocator()
        super().__init__(driver)  
    
    def click_simple_checkbox(self):
        self.find_element(*self.locator.SINGLE_CHECKBOX).click()

    def get_simple_result(self):
        return self.find_element(*self.locator.SINGLE_CHECKBOX_RESULT).text

    def click_checkbox1(self):
        self.find_element(*self.locator.MULTI_CHECKBOX_1).click()

    def click_checkbox2(self):
        self.find_element(*self.locator.MULTI_CHECKBOX_2).click()

    def click_checkbox3(self):
        self.find_element(*self.locator.MULTI_CHECKBOX_3).click()

    def click_checkbox4(self):
        self.find_element(*self.locator.MULTI_CHECKBOX_4).click()

    def click_check_all(self):
        self.find_element(*self.locator.MULTI_CHECKBOX_ALL).click()

    def get_check_all_attribute(self):
        return self.find_element(*self.locator.MULTI_CHECKBOX_ALL).get_attribute("value")

    def is_selected_checkbox1(self):
        return self.find_element(*self.locator.MULTI_CHECKBOX_1).is_selected()
            
    def is_selected_checkbox2(self):
        return self.find_element(*self.locator.MULTI_CHECKBOX_2).is_selected()

    def is_selected_checkbox3(self):
        return self.find_element(*self.locator.MULTI_CHECKBOX_3).is_selected()

    def is_selected_checkbox4(self):
        return self.find_element(*self.locator.MULTI_CHECKBOX_4).is_selected()
    