import unittest
from selenium import webdriver
from Pages.InputFormPage import InputFormPage
from Helpers.GlobalVariable import EXECUTABLE_PATH
from behave import given, when, then 

# Global

@given(u'user is on selenium simple input page')
def selenium_page(context):
    driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
    context.page = InputFormPage(driver)
    context.page.open('basic-first-form-demo.html')
    assert context.page.get_url() == "https://www.seleniumeasy.com/test/basic-first-form-demo.html"

@then(u'page is closed')
def close_page(context):
    context.page.driver.close()



# Scenario Simple Input

@when(u'write {thing} in input form')
def write_thing(context, thing):
    value = thing if thing != 'empty' else ""
    context.page.enter_message(value)
        
@when(u'click submit button')
def submit(context):
    context.page.click_submit_button()
        
@then(u'{thing} is displayed')    
def check_result(context, thing):
    result = thing if thing != 'empty' else ""
    assert context.page.get_message_result() == result



# Scenario Two input form

@when(u'user has entered {number1} into the first form')
def enter_first_number(context, number1):
    value = number1 if number1 != 'empty' else ""
    context.page.enter_a(value)

@when(u'user has also entered {number2} into second form')
def enter_sec_number(context, number2):
    value = number2 if number2 != 'empty' else ""
    context.page.enter_b(value)

@when(u'user press add')
def sumbit(context):
    context.page.click_submit_ab_button()

@then(u'the result should be {result}')
def check_ab_result(context, result):
    result = result if result != 'empty' else ""
    assert context.page.get_ab_result() == result