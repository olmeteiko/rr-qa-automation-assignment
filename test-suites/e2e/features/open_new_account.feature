Feature: User registration and opening an account


    Scenario: A user registers into the ParaBank system and opens an account
        Given a new customer, "Alice"
        And "Alice" registers
        When "Alice" registers a new "savings" account
        And opens the "Account Overview" page
        Then there is an amount of "100" on the "savings" account