Feature: Table Filter page
    
    Scenario Outline: Display only one color page
        Given user is on selenium table filter page
        And all colors records are displayed
        When user click <color> filter
        Then there are displayed only <color> records
        And page is closed

        Examples:
        | color  |  
        | Green  |
        | Orange |
        | Red    |
        | all    |
    

    