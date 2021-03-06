# Created by Effortis at 12/24/2018
Feature: Ad Design actions
  As an ad creator
  I want to be able to perform some actions
  when I hover over an existing ad design

  Scenario: Hover Over Ad Design
    Given I am on Ad Design page
    And At least one ad design is created
    When I hover over the ad design
    Then I should see 5 action icons

  Scenario: Duplicate Ad design
    Given I am on Ad Design page
    And At least one ad design is created
    When I hover over the ad design
    And I click on Duplicate icon
    Then 'Duplicate' notification is displayed
    And The ad is duplicated

  Scenario: Move Ad Design to a Folder - Negative
    Given I am on Ad Design page
    And At least one ad design is created
    When I hover over the ad design
    And I click on Move To Folder icon
    And I click on Move button
    Then The popup stays displayed

  Scenario: Move Ad Design to a Folder - Positive
    Given I am on Ad Design page
    And At least one ad design is created
    And At least one folder is created
    When I hover over the ad design
    And I click on Move To Folder icon
    And I select a folder and click on Move
    Then The ad is moved into the folder

  Scenario: Edit Ad Design
    Given I am on Ad Design page
    And At least one ad design is created
    And At least one folder is created
    When I hover over the ad design
    And I click on Edit icon
    Then The edit popup is opened

  Scenario Outline: Ad Design Preview
    Given I am on Ad Design page
    When I hover over the ad design of type <type>
    And I click on Preview icon
    Then The Preview popup is opened
    And All the previews display properly

    Examples: Types
    | type          |
    | Page Like Ad  |
    | Page Post Ad  |
    | Link Ad       |
    | Lead Ad       |
    | Photo Ad      |
    | Video Ad      |

  Scenario: Delete Ad Design
    Given I am on Ad Design page
    And At least one ad design is created
    When I hover over the ad design
    And I click on Delete icon
    Then 'Delete' notification is displayed
    And The ad is deleted

  Scenario: Select Ad Designs
    Given I am on Ad Design page
    And At least one ad design is created
    When I hover over the ad designs and click Select
    Then The ad designs are selected

  Scenario: Unselect Multiple Ad Designs
    Given I am on Ad Design page
    And At least two ad designs are selected
    When I click on Unselect all link
    Then The ad designs are unselected

  Scenario: Move Multiple Ad Designs to a Folder
    Given I am on Ad Design page
    And At least two ad designs are created
    And At least one folder is created
    When I click on Move to
    And Choose a folder
    Then The ad designs are moved to that folder