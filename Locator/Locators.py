from selenium.webdriver.common.by import By

class InputFormPageLocator(object):
    MESSAGE_INPUT       = (By.XPATH, '//*[@id="user-message"]')
    MESSAGE_BUTTON      = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
    MESSAGE_RESULT      = (By.XPATH, '//*[@id="display"]')

    INPUT_A             = (By.XPATH, '//*[@id="sum1"]')
    INPUT_B             = (By.XPATH, '//*[@id="sum2"]')
    BUTTON              = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
    RESULT              = (By.XPATH, '//*[@id="displayvalue"]')


class CheckBoxPageLocator(object):
    SINGLE_CHECKBOX         = (By.XPATH, '//*[@id="isAgeSelected"]') 
    SINGLE_CHECKBOX_RESULT  = (By.XPATH, '//*[@id="txtAge"]') 

    MULTI_CHECKBOX_1        = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/label/input')
    MULTI_CHECKBOX_2        = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/label/input')
    MULTI_CHECKBOX_3        = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[3]/label/input')
    MULTI_CHECKBOX_4        = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[4]/label/input')
    MULTI_CHECKBOX_ALL      = (By.XPATH, '//*[@id="check1"]')


class RadioButtonPageLocator(object):
    GENDER_RADIO_FEMALE     = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/label[2]/input') 
    GENDER_RADIO_MALE       = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/label[1]/input') 
    GENDER_SUBMIT_BUTTON    = (By.XPATH, '//*[@id="buttoncheck"]') 
    GENDER_RESULT           = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[2]/p[3]') 

    RADIO_MALE              = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/label[1]/input') 
    RADIO_FEMALE            = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/label[2]/input') 
    RADIO_AGE_0_5           = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/label[1]/input') 
    RADIO_AGE_5_15          = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/label[2]/input') 
    RADIO_AGE_15_50         = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/label[3]/input') 
    RADIO_SUBMIT_BUTTON     = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/button') 
    RADIO_RESULT            = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/p[2]') 


class AjaxFormPageLocators(object):
    NAME            = (By.XPATH, '//*[@id="title"]')
    TEXT            = (By.XPATH, '//*[@id="description"]')
    BUTTON          = (By.XPATH, '//*[@id="btn-submit"]')
    RESULT          = (By.XPATH, '//*[@id="submit-control"]')


class TableFilterPageLocator(object):
    GREEN_BUTTON        = (By.XPATH, '/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[1]')
    RED_BUTTON          = (By.XPATH, '/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[3]')
    ORANGE_BUTTON       = (By.XPATH, '/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[2]')
    ALL_BUTTON          = (By.XPATH, '/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[4]')
    GREEN_RECORD        = (By.XPATH, '/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/h4/span')
    RED_RECORD          = (By.XPATH, '/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[2]/table/tbody/tr[3]/td[3]/div/div/h4/span')
    ORANGE_RECORD       = (By.XPATH, '/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/div/div/h4/span')
        