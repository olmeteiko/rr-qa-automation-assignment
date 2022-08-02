from behave import *
from testkit.api import parabank

from .unregistered_customer import *
from .registered_customer import *
from .invalid_password import *


@when('"{customer_name}" logs in')
def step_impl(context, customer_name):
    customer = context.customers[customer_name]
    try:
        response = parabank.login(customer)
        context.customer_login_response = response
        context.request_error = None
    except parabank.ApiError as err:
        context.request_error = err


@then('an error occurs')
def step_impl(context):
    err = context.request_error
    assert err is not None


@then('no error is returned')
def step_impl(context):
    err = context.request_error
    assert err is None
