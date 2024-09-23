
Feature: Withdrawal Functionality

  Scenario: User can Withdrawal Successfully
    Given Open Bank App
    When Enter Valid User ID mngr591312
    And Enter Valid Password gatyvEp
    And Click Login
    And Click Withdrawal
    And Enter Account No 138547
    And Enter Amount 500 dollars
    And Enter Description cash
    And Click Submit
    Then Verify Withdrawal Is Successful
