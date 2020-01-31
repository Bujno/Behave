import unittest
from selenium import webdriver
from Pages.AjaxFormPage import AjaxFormPage
from Helpers.GlobalVariable import EXECUTABLE_PATH
from behave import given, when, then 
import time

# Global

@given(u'user is on selenium ajax form page')
def selenium_page(context):
    driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
    context.page = AjaxFormPage(driver)
    context.page.open('ajax-form-submit-demo.html')
    assert context.page.get_url() == "https://www.seleniumeasy.com/test/ajax-form-submit-demo.html"


# Scenario Check ajax form

@when(u'write {name} in name input')
def write_name(context, name):
    value = name if name != 'empty' else ""
    context.page.enter_name(value)

@when(u'write {comment} in comment input')
def write_comment(context, comment):
    value = comment if comment != 'empty' else ""
    context.page.enter_text(value)
        
@when(u'click sumbit ajax form button')
def submit(context):
    context.page.click_submit_button()

@then(u'ajax page is loading')
def loaging_page(context):
    time.sleep(2)
        
@then(u'message {is_displayed}')    
def check_result(context, is_displayed):
    result = 'Form submited Successfully!' if is_displayed == 'displayed' else ""
    assert context.page.get_result() == result
