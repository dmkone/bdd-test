# Created by Effortis at 12/6/2018
@wip
Feature: Photo Ad Creation Screen
  As an admin user
  I want to open Photo Ad creation screen
  So that I can create Photo Ads

  Scenario: Open the Photo Ad creation screen
    Given Ad Design creation popup is opened
    When I select an Ad Account from adaccount drop-down
    And I select a page
    And I click on Photo Ad box
    And I click on "Next" button
    Then I should see Photo Ad creation screen

  Scenario: Create a photo ad - positive
    Given I am on Photo Ad creation screen
    When I upload an image
    And I click on "Create" button
    Then I should see the newly created Photo Ad design

  Scenario: Create a photo ad - negative
    Given I am on Photo Ad creation screen
    When I click on "Create" button
    Then I should see a validation error "Field is required"