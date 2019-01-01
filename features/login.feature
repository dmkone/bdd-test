# Created by Effortis at 12/5/2018
@wip
Feature: Login Functionality
  # Check login functionality

  Scenario: Positive login
    Given I am on login page
    When I type correct username in the username field
    And I type correct password in the password field
    And I click the Login button
    Then I am logged in

  Scenario: Negative login
    Given I am on login page
    When I type wrong username in the username field
    And I type any password in the password field
    And I click the Login button
    Then I see error notification