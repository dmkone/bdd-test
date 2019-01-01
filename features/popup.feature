# Created by Effortis at 12/4/2018

Feature: Ad Designs Popup
  As an admin user
  I want to open "Ad Designs" popup
  So that I can create ad designs

  Scenario: Go To Ad Design Page
    Given I am logged in
    When I click on "Ad Designs" tab
    Then I should see Ad Design page

  Scenario: Create Ad Design
    Given I am on Ad Design page
    When I click on "Create Ad Design" button
    Then I should see a popup for Ad Design creation
