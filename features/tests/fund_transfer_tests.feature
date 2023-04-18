
Feature: Verifying Fund Transfers

  Scenario: Verify Fund Transfers
    Given Open Bank App
    When Enter Valid User ID mngr489998
    And Enter Valid Password tamuhUb
    And Click Login
    And Click Fund Transfer
    And Input Correct Required Fields For Fund Transfer
    And Click Submit
    Then Verify Fund Transfer Successful

  Scenario: Verify Fund Transfer is not done again when page is reloaded
    Given Open Bank App
    When Enter Valid User ID mngr489998
    And Enter Valid Password tamuhUb
    And Click Login
    And Click Fund Transfer
    And Input Correct Required Fields For Fund Transfer
    And Click Submit
    Then Verify Page Is Redirecting To Fund Transfer Page

  Scenario: Verify system when Manager enters wrong Account number during Fund Transfer
    Given Open Bank App
    When Enter Valid User ID mngr489998
    And Enter Valid Password tamuhUb
    And Click Login
    And Click Fund Transfer
    And Input Incorrect Required Fields For Fund Transfer
    And Click Submit
    Then Verify A Pop - UP Account 555555does not exist!!! is visible