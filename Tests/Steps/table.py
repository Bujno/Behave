from selenium import webdriver
from Pages.TableFilterPage import TableFilterPage
from Helpers.GlobalVariable import EXECUTABLE_PATH
from behave import given, when, then 
import time

@given(u'user is on selenium table filter page')
def selenium_page(context):
    driver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)
    context.page = TableFilterPage(driver)
    context.page.open('table-records-filter-demo.html')
    assert context.page.get_url() == "https://www.seleniumeasy.com/test/table-records-filter-demo.html"

@given(u'all colors records are displayed')
@then(u'all colors records are displayed')
def display_all(context):
    assert True == context.page.is_displayed_green_record()
    assert True == context.page.is_displayed_red_record()
    assert True == context.page.is_displayed_orange_record()
    


@when(u'user click {color} filter')
def click_color(context, color):
    if color == 'Green':
        context.page.click_green_button()
    elif color == 'Orange':
        context.page.click_orange_button()
    elif color == 'Red':
        context.page.click_red_button()
    elif color == 'all':
        context.page.click_all_button()



@then(u'there are displayed only {color} records')
def radiobutton_submit(context, color):
    if color == 'Green':
        assert True == context.page.is_displayed_green_record()
        assert False == context.page.is_displayed_red_record()
        assert False == context.page.is_displayed_orange_record()
    elif color == 'Orange':
        assert False == context.page.is_displayed_green_record()
        assert False == context.page.is_displayed_red_record()
        assert True == context.page.is_displayed_orange_record()
    elif color == 'Red':
        assert False == context.page.is_displayed_green_record()
        assert True == context.page.is_displayed_red_record()
        assert False == context.page.is_displayed_orange_record()
    elif color == 'All':
        display_all(context)

