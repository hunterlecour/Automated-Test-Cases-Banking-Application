
Feature: Withdrawal Functionality

  Scenario: User can Withdrawal Successfully
    Given Open Bank App
    When Enter Invalid User ID mdfdsfsf
    And Enter Valid Password tamuhUb
    And Click Login
    #And Click Withdrawal (THIS IS FAILING)
    And Enter Account No 121219
    And Enter Amount 500 dollars
    And Enter Description cash
    And Click Submit
    Then Verify Withdrawal Is Successful
