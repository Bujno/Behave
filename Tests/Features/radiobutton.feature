Feature: Radiobutton Page
    
    Scenario Outline: Simple radiobutton
        Given user is on selenium radiobutton page
        When user click on <radiobutton_type> simple radiobutton
        Then user click on simple radiobutton submit button
        And radiobutton message <message>
        And page is closed

        Examples:
        | radiobutton_type   | message          | 
        | Male               | is displayed     | 
        | Female             | is displayed     | 
        | none               | is not displayed |
    
    Scenario Outline: Multiple radiobuttons
        Given user is on selenium radiobutton page
        When user click on <sex> choice radiobutton
        And user click on <age> radiobutton
        Then user click on multiple radiobuttons submit button
        And multiple radiobuttons message shows
        And page is closed

        Examples:
        | sex       | age      | 
        | Male      | 0 - 5    |
        | Male      | 5 - 15   |
        | Male      | 15 - 50  |
        | Female    | 0 - 5    |
        | Female    | 5 - 15   |
        | Female    | 15 - 50  |

    

    