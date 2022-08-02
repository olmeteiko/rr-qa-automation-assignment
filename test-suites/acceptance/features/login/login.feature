Feature: ParaBank Customer login
    To perform customer account-related operations, the customer should log into the system.


    Scenario: Unregistered customer attempts to login
        Given an unregistered customer, "Alice"
        When "Alice" logs in
        Then an error occurs


    Scenario: Customers' data is returned on a successful login
        Given a registered customer, "Robert"
        When "Robert" logs in
        Then "Robert" customer data matches the response


    Scenario: Customer's sequential login attempts succeed
    The customer's sequential log-in attempts do not lead to error, and
    there is no need to log out of the system before logging in.

        Given a registered customer, "Robert"
        When "Robert" logs in
        And "Robert" logs in
        Then no error is returned
        And "Robert" customer data matches the response


    Scenario: A registered customer cannot log-in with an incorrect password
        Given a registered customer, "Robert"
        When "Robert" logs in with an incorrect "password"
        Then an error occurs