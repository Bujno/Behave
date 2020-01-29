Feature: Selenium simple input page

  Scenario Outline: Simple input
    Given user is at selenium simple input page
    When write <thing> in input form
    And  click submit button
    Then <thing> are displayed
    And page is closed

       Examples:
        | thing       |
        | Test        |
        | Hello World |


  Scenario Outline: Two input form
    Given user is at selenium simple input page
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


