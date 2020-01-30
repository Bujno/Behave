from selenium import webdriver
from Pages.CheckboxPage import CheckboxPage
from Helpers.GlobalVariable import EXECUTABLE_PATH
from behave import given, when, then 
import time

@given(u'user is on selenium checkbox page')
def selenium_page(context):
    driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
    context.page = CheckboxPage(driver)
    context.page.open('basic-checkbox-demo.html')
    assert context.page.get_url() == "https://www.seleniumeasy.com/test/basic-checkbox-demo.html"



@when(u'user checked checkbox')
@then(u'user checked checkbox')
def simple_checkbox(context):
    context.page.click_simple_checkbox()

@when(u'user clicked {number} checkboxes')
def write_comment(context, number):
    context.number = number
    if int(number) >= 1:
        context.page.click_checkbox1()
    if int(number) >= 2:
        context.page.click_checkbox2()
    if  int(number) >= 3:
        context.page.click_checkbox3()
    if int(number) == 4:
        context.page.click_checkbox4()

@when(u'user clicked multiple checkbox button')
@then(u'user clicked multiple checkbox button')
def check_all(context):
    context.page.click_check_all()



@then(u'checkbox message is displayed')
def display_message(context):
    assert "Success - Check box is checked" == context.page.get_simple_result()
        
@then(u'checkbox message is not displayed')    
def dont_display_message(context):
    assert "" == context.page.get_simple_result()

@then(u'checkboxes are checked')
def check_checkboxes(context):
    if int(context.number) == 1:
        assert True == context.page.is_selected_checkbox1()
        assert False == context.page.is_selected_checkbox2()
        assert False == context.page.is_selected_checkbox3()
        assert False == context.page.is_selected_checkbox4()
    elif int(context.number) == 2:
        assert True == context.page.is_selected_checkbox1()
        assert True == context.page.is_selected_checkbox2()
        assert False == context.page.is_selected_checkbox3()
        assert False == context.page.is_selected_checkbox4()
    elif int(context.number) == 3:
        assert True == context.page.is_selected_checkbox1()
        assert True == context.page.is_selected_checkbox2()
        assert True == context.page.is_selected_checkbox3()
        assert False == context.page.is_selected_checkbox4()
    elif int(context.number) == 4:
        assert True == context.page.is_selected_checkbox1()
        assert True == context.page.is_selected_checkbox2()
        assert True == context.page.is_selected_checkbox3()
        assert True == context.page.is_selected_checkbox4()

@then(u'text on button {has_changed}')
def change_text(context, has_changed):
    if has_changed == 'has changed':
        assert 'Uncheck All' == context.page.get_check_all_attribute()
    else:
        assert 'Check All' == context.page.get_check_all_attribute()

@then(u'all checkboxes are checked')
def all_checked(context):
    assert True == context.page.is_selected_checkbox1()
    assert True == context.page.is_selected_checkbox2()
    assert True == context.page.is_selected_checkbox3()
    assert True == context.page.is_selected_checkbox4()

@then(u'all checkboxes are unchecked')
def all_unchecked(context):
    assert False == context.page.is_selected_checkbox1()
    assert False == context.page.is_selected_checkbox2()
    assert False == context.page.is_selected_checkbox3()
    assert False == context.page.is_selected_checkbox4()
