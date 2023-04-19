
Feature: Withdrawal Functionality

  Scenario: User can Withdrawal Successfully
    Given Open Bank App
    When Enter Valid User ID mngr489998
    And Enter Valid Password tamuhUb
    And Click Login
    And Click Withdrawal
    And Enter Account No 121995
    And Enter Amount 500 dollars
    And Enter Description cash
    And Click Submit
    Then Verify Withdrawal Is Successful
