Feature: Acquisition

  Scenario: Creating an acquisition
    Given a client exists
    And a filled-in track exists
    When a user creates an acquisition
    Then the acquisition is saved in the database

  Scenario: Submitting an acquisition with a form
    Given a client exists
    And a filled-in track exists
    When a user submits a valid acquisition form
    Then the acquisition is saved in the database
