Feature: Test Scenarios for Search functionality of soft.reelly page

  @smoke
  Scenario: User login main page and verify switch page functionality
    Given Open soft.reelly page
    And Login to the page
    And Click on continue button
    And Store original window
    And Click on “Connect the company”
    And Switch to new window
    And Verify the right tab opens
    And Close the current page and switch back
