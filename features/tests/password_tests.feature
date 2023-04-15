
Feature: Change Password

  Scenario: Enter incorrect Old Password
    Given Open Bank App
    When Enter Valid User ID mngr489998
    And Enter Valid Password tamuhUb
    And Click Login
    And Click Change Password
    And Enter Incorrect Old Password 555%
    And Enter New Password Credentials 777&
    And Click Submit
    Then Verify User Is Unable to Change Password
