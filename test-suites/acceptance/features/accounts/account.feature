@wip
Feature: Account features


  Scenario: Request for a not-existing account returns an error
    Given a registered customer, "Robert"
    When "Robert" requests a not-existing account
    Then an error is returned


  Scenario: Request for an existing account return an account info
    Given a registered customer, "Robert"
    When "Robert" requests an existing account
    Then the account data is returned


  Scenario: Request for an account of another customer
    Given a registered customer, "Alice"
    And a registered customer, "Robert"
    When "Alice" requests "Bob" "checking" account
    Then an error is returned
