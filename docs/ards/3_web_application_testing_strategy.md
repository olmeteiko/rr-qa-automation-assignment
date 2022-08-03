# 3. UI-Application End-to-End Testing

## Status

Formulated, Testing framework is partially implemented

## Context

According to the [global testing strategy](./1_testing_strategy.md), the UI-Application testing suite is to be implemented as an End-to-End one. The functionality will be assessed from the customers' point of view, focusing on the customer's intentions.

## Decision

The test suite will be implemented as a BDD-test suite capturing all the business-critical user action flows.

#### Tech stack

* JavaScript (TypeScript)
* [Cucumber-JS](https://github.com/cucumber/cucumber-js)
* [Selenium Web-Driver](https://www.selenium.dev/selenium/docs/api/javascript/index.html)

Using **CucumberJS** allows to capture all testing scenarios in the form of requirements.

The **TypeScript** is chosen to be evaluated as an alternative to the Python (which was used for the acceptance test suite).

## Consequences

TBD after implementation and probation.
