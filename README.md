# Behave

## To install 
```
pip install -r requirements.txt
```
## To do

```
 def page_has_loaded(self):
        page_state = self.browser.execute_script('return document.readyState;')
        return page_state == 'complete'

def test020_user_login(self):
        self.page.click_pln_btc_link()
        while(not self.page_has_loaded()):
            pass
        self.assertEqual(self.browser.current_url, url)
```

## Found ERRORS
```
Should be

Feature: Selenium simple input page
  Scenario: Two input form
     Given user is at selenium simple input page
     When user has entered *12* into the first form
     And user has also entered *512w1* into second form
     And user press add
     Then the result should be *NaN*
     And page is closed
     
     
Insted of

Feature: Selenium simple input page
  Scenario: Two input form
     Given user is at selenium simple input page
     When user has entered *12* into the first form
     And user has also entered *512w1* into second form
     And user press add
     Then the result should be *524*
     And page is closed
    
```

```
Should be

Feature: Ajax form page
  Scenario:  Check ajax form
     Given user is at selenium ajax form page
     When write *only name* in name input
     And write *empty* in comment input
     And click sumbit ajax form button 
     Then ajax page is loading
     And message *not_displayed*
     And page is closed
     
     
Insted of

Feature: Ajax form page
  Scenario:  Check ajax form
     Given user is at selenium ajax form page
     When write *only name* in name input
     And write *empty* in comment input
     And click sumbit ajax form button 
     Then ajax page is loading
     And message *displayed*
     And page is closed
```
