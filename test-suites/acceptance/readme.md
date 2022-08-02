# Acceptance Test Suite

#### Directory structure

```yaml
features/                          # Requirements grouped in directories.
    accounts/                      # Accounts' scenarios. Not implemented, just
                                   # conceptualised.
    login/                         # Customer's login-related scenarios.
    steps/                         # Requirement steps bindings to the testing 
                                   # code.
testkit/                           # Test-suite adapters that abstract-out 
                                   # transport and domain logic from the tests.
    api/parabank                   # The ParaBank connector. 
    model/                         # Contains the domain DTOs.
```

#### Further improvements 
* The `features/steps/` directory placement is the recommended way of organising the Behave test suite, but I would extract it not to mix the requirements suite and the steps binding together.
* For now, the API error-handling and assertion are simplified but should be extended.


#### Running instructions

```sh
# Run all the scenarios.
behave

# Ignore work-in-progress-scenarios.
behave --tags ~@wip -k

# Generate the basic test report.
behave -f html --tags ~@wip -k  -o behave-report.html
```

