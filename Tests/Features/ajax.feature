Feature: Ajax form page

    Scenario Outline: Check ajax form
        Given user is at selenium ajax form page
        When write <name> in name input
        And write <comment> in comment input
        And click sumbit ajax form button 
        Then ajax page is loading
        And message <is_displayed>
        And page is closed

            Examples:
                | name        | comment         | is_displayed  |
                | Test        | Testing comment | displayed     |
                | empty       | only comment    | not displayed |
                | only name   | empty           | displayed     |
                | empty       | empty           | not displayed |

# should be 'not displayed' - ERROR in line 16
        
    
    