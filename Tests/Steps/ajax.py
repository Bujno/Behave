import unittest
from selenium import webdriver
from Pages.AjaxFormPage import AjaxFormPage
from Helpers.GlobalVariable import EXECUTABLE_PATH
from behave import given, when, then 
import time

# Global

@given(u'user is at selenium simple ajax form page')
def selenium_page(context):
    driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
    context.page = AjaxFormPage(driver)
    context.page.open('ajax-form-submit-demo.html')
    assert context.page.get_url() == "https://www.seleniumeasy.com/test/ajax-form-submit-demo.html"

# @then(u'page is closed')
# def close_page(context):
#     context.page.driver.close()



# Scenario Ajax valid form

@when(u'write {name} in name input')
def write_name(context, name):
    context.page.enter_name(name)

@when(u'write {comment} in comment input')
def write_comment(context, comment):
    context.page.enter_text(comment)
        
@when(u'click sumbit ajax button')
def submit(context):
    context.page.click_submit_button()

@then(u'page is loading')
def loaging_page(context):
    time.sleep(2)
        
@then(u'message is displayed')    
def check_result(context):
    assert context.page.get_result() == 'Form submited Successfully!'



# Scenario Ajax invalid form

@then(u'message is not displayed')    
def check_no_result(context):
    assert context.page.get_result() == ''
