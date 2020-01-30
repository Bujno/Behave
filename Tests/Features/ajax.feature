Feature: Ajax form page

    Scenario Outline: Ajax valid form
        Given user is at selenium simple ajax form page
        When write <name> in name input
        And write <comment> in comment input
        And click sumbit ajax button 
        Then page is loading
        And message is displayed
        And page is closed

            Examples:
                | name        | comment         |
                | Test        | Testing comment |
                | Hello World | 123123123       |

    Scenario Outline: Ajax invalid form
        Given user is at selenium simple ajax form page
        When page is loading
        And message is not displayed
        And page is closed
        
        
    
    