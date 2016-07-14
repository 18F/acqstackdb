Feature: Clients

  Scenario: Creating a client
    Given an agency exists
    When a user creates a subagency
    Then the subagency is saved in the database

  Scenario: Submitting a client with a form
    Given an agency exists
    When a user submits a valid subagency form
    Then the subagency is saved in the database
