# End-to-End Test Suite

### Directory structure
```yaml
features/                          # End-to-end feature requirements.
step_definitions/                  # Test-suite step definitions.
    stepdefs.ts                    # Test-suite step bindings.
    testkit/                       # The draft for the testing framework.
        lib/                       # The abstractions for the UI testing.
        models/                    # The DTOs for the domain entities.
        pages/                     # The PageObjectModels abstractions over 
                                   # the application pages.
```

### Test suite status 
This test suite is not complete but shows the general idea and abstraction layers for the full-fledged End-to-End test suite.

This section's main focus was to showcase the foundation of the testing framework, which is why the test coverage is left out of the scope for this task. 

### Further steps
* 
* separate the `step_definitions` and the `testkit` packages;
* add support for more HTML primitives (for now only Input and Button are supported);
* elaborate on the `models` package to include all business entities;
* add support for all the application pages;

### Running instructions
```sh
# Run the cucumber-js runner.
npm test
```
