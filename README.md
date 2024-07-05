
Feature: Test Scenarios for Search functionality of soft.reelly page
  Scenario: User sign on main page functionality
    Given Open soft.reelly page
    When Input name field
    Then Input phone field
    And Input pwd field
    And Input comp_web field
    And Choose role field
    And Choose country field
    And Choose comp_size field
    And Verify expected URL
