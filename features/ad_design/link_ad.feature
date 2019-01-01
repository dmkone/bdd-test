# Created by Davit at 12/5/2018
@wip
Feature: Link Ad Creation Screen
  As an admin user
  I want to open Link Ad creation screen
  So that I can create Link Ads

  Scenario: User opens the Link Ad screen
    Given Ad Design creation popup is opened
    When I select an Ad Account from adaccount drop-down
    And I select a page
    And I click on Link Ad box
    And I click on "Next" button
    Then I should see Link Ad creation screen

  Scenario: Create single image link ad
    Given I am on Link Ad creation screen
    When I click on "Single Image" box
    And I upload an image
    And I fill in the required URL field
    And I click on "Create" button
    Then I should see the newly created Link Ad design

  Scenario: Create single video ad
    Given I am on Link Ad creation screen
    When I click on "Single Video" box
    And I upload a video
    And I fill in the required URL field
    And I click on "Create" button
    Then I should see the newly created Link Ad design

  Scenario: Create slideshow ad
    Given I am on Link Ad creation screen
    When I click on "Slideshow" box
    And I upload images
    And I fill in the required URL field
    And I click on "Create" button
    Then I should see the newly created Link Ad design

   Scenario: Create a link ad - negative
    Given I am on Link Ad creation screen
    When I click on "Create" button
    Then I should see a validation error "Field is required"