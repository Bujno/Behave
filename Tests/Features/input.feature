Feature: Selenium simple input page

  Scenario Outline: Simple input
    Given user is on selenium simple input page
    When write <thing> in input form
    And  click submit button
    Then <thing> is displayed
    And page is closed

       Examples:
        | thing       |
        | Test        |
        | Hello World |
        | empty       |


  Scenario Outline: Two input form
    Given user is on selenium simple input page
    When user has entered <number1> into the first form
     And user has also entered <number2> into second form
     And user press add
     Then the result should be <result>
     And page is closed

        Examples:
            |  number1|  number2|   result|
            |        5|        2|        7|
            |        4|        8|       12|  
            |        1|        c|      NaN|
            |       12|    512w1|      524| 
            |    empty|        8|      NaN|  
            |        1|    empty|      NaN|
            |    empty|    empty|      NaN|
            |   string|   string|      NaN|

# should be NaN - ERROR in line 30