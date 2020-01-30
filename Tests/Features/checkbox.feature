Feature: Checkbox selenium page
    
    Scenario: Simple checkbox clicked once
        Given user is on selenium checkbox page
        When user checked checkbox
        Then checkbox message is displayed
        And page is closed

    Scenario: Simple checkbox clicked twice
        Given user is on selenium checkbox page
        When user checked checkbox
        Then checkbox message is displayed
        And user checked checkbox
        And checkbox message is not displayed 
        And page is closed

    Scenario Outline: Multiple checkbox
        Given user is on selenium checkbox page
        When user clicked <number> checkboxes
        Then checkboxes are checked
        And text on button <has_changed>
        And page is closed

        Examples:
        | number    | has_changed       | 
        | 1         | hasn't changed    | 
        | 2         | hasn't changed    |
        | 3         | hasn't changed      |
        | 4         | has changed    |
        | 0         | hasn't changed    |

    Scenario: Multiple chceckbox checked and unchecked by button
        Given user is on selenium checkbox page
        When user clicked multiple checkbox button
        Then all checkboxes are checked
        And user clicked multiple checkbox button
        And all checkboxes are unchecked
        And page is closed
    

    

    
    

    