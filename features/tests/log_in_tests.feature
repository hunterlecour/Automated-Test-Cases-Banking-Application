
Feature: Verify the Login Section


  Scenario: Enter valid userid & password
    Given Open Bank App
    When Enter Valid User ID mngr489998
    And Enter Valid Password tamuhUb
    And Click Login
    Then Verify Login Is Successful

  Scenario: Enter invalid userid & valid password
    Given Open Bank App
    When Enter Invalid User ID mdfdsfsf
    And Enter Valid Password tamuhUb
    And Click Login
    Then Verify Login is Unsuccessful

  Scenario: Enter valid userid & invalid password
    Given Open Bank App
    When Enter Valid User ID mngr489998
    And Enter Invalid Password sdfkdsf
    And Click Login
    Then Verify Login is Unsuccessful

  Scenario: Enter invalid userid & invalid password
    Given Open Bank App
    When Enter Invalid User ID mdfdsfsf
    And Enter Invalid Password skjdfndsnf
    And Click Login
    Then Verify Login is Unsuccessful

  Scenario: Verify User Can Log Out
    Given Open Bank App
    When Enter Valid User ID mngr489998
    And Enter Valid Password tamuhUb
    And Click Login
    And Click Logout
    Then Verify User Can Log Out



