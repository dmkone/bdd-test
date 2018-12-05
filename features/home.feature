Feature: Homepage

  Scenario Outline: Components
    Given I load the website
    Then I see a page with title <title>

    Examples:
      | title                        |
      | Custom Marketing Automation  |