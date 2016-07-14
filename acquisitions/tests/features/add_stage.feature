Feature: Stages

  Scenario: Creating a stage
    Given an database is created
    When a user creates a stage
    Then the stage is saved in the database

  Scenario: Submitting a stage with a form
    Given an database is created
    When a user submits a valid stage form
    Then the stage is saved in the database

  Scenario: Re-ordering a stage
    Given two or more stages exist
    And the stages are in an order
    When a user clicks a button to move the stage up
    Then the stage should move up one slot in the order
