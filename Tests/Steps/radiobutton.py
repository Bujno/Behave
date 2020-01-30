from selenium import webdriver
from Pages.RadioButtonPage import RadioButtonPage
from Helpers.GlobalVariable import EXECUTABLE_PATH
from behave import given, when, then 
import time

@given(u'user is on selenium radiobutton page')
def selenium_page(context):
    driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
    context.page = RadioButtonPage(driver)
    context.page.open('basic-radiobutton-demo.html')
    assert context.page.get_url() == "https://www.seleniumeasy.com/test/basic-radiobutton-demo.html"



@when(u'user click on {radiobutton_type} simple radiobutton')
def simple_radiobutton(context, radiobutton_type):
    context.type = radiobutton_type
    if context.type == 'Male':
        context.page.click_radio_male()
    if context.type == 'Female':
        context.page.click_radio_female()
    
@when(u'user click on {sex} choice radiobutton')
def sex_radiobutton(context, sex):
    context.sex = sex
    if sex == 'Female':
        context.page.click_radio_group_female()
    if sex == 'Male':
        context.page.click_radio_group_male()

@when(u'user click on {age} radiobutton')
def age_radiobutton(context, age):
    context.age = age
    if age == '0 - 5':
        context.page.click_radio_age_0_5()
    if age == '5 - 15':
        context.page.click_radio_age_5_15()
    if age == '15 - 50':
        context.page.click_radio_age_15_50()



@then(u'user click on simple radiobutton submit button')
def radiobutton_submit(context):
    context.page.click_submit_button()

@then(u'radiobutton message {message}')
def display_message(context, message):
    if message == 'is displayed':
        assert f"Radio button '{context.type}' is checked" == context.page.get_result_text()
    else:
        assert "Radio button is Not checked" == context.page.get_result_text()

@then(u'user click on multiple radiobuttons submit button')
def submit_radio(context):
    context.page.click_radio_group_btn()

@then(u'multiple radiobuttons message shows')
def show_message(context):
    message = 'Sex : {0}\nAge group: {1}'.format(context.sex, context.age)
    assert message == context.page.get_radio_group_result_text()