# 2. Web-Service API testing

## Status

Formulated, Partially implemented

## Context

According to the [global testing strategy](./1_testing_strategy.md), the Web-Service API testing suite is to be implemented as an acceptance one. All the endpoints actions are to be covered with expected behaviour, capturing all-business relevant activities and expectations.

## Decision

The test suite is to be implemented as a BDD-test suite capturing all the expected behaviour from the Web-Service API. 

#### Tech stack

* Python
* [Behave](https://behave.readthedocs.io/en/stable/)
* [Swagger OpenAPI client](https://editor.swagger.io)

Using **Behave** allows to capture all business expectations from the Web-Service and to rely on this acceptance suite in further regression testing.

Another benefit of using the Behave is the freedom of the test result transformation as there are plenty of solutions for test results visualisations.

**Swagger OpenAPI** client is used as a mediator to perform requests to the ParaBank Web-Service. It provides compliance with the backend contract. Nevertheless, the level of abstraction is not sufficient. That is why it is additionally wrapped with a test-level adapter to make the tests cleaner and detached from the transport layer.



![](media/acceptance_test_suite.png)

## Consequences

TBD after implementation and probation.

#### Problem

The complete automation for this test suite is impossible in the current API implementation due to the lack of  a customer creation endpoint. It must be implemented and exposed for the QA team to cover all the expectations on this test suite.



## Further extentions

* versioning — align the versioning of the system under test and the client used for communication to the API;
* tags clustering — mark scenarios with relevant tags for further clustering into functionality groups.