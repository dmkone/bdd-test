# Created by Effortis at 12/6/2018
@wip
Feature: Video Ad Creation Screen
  As an admin user
  I want to open Video Ad creation screen
  So that I can create Video Ads

  Scenario: Open the Video Ad creation screen
    Given Ad Design creation popup is opened
    When I select an Ad Account from adaccount drop-down
    And I select a page
    And I click on Video Ad box
    And I click on "Next" button
    Then I should see Video Ad creation screen

  Scenario: Create a video ad - positive
    Given I am on Video Ad creation screen
    When I upload a video
    And I click on "Create" button
    Then I should see the newly created Video Ad design