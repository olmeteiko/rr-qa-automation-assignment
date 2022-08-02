from behave import *
from testkit.api import parabank


@given('a registered customer, "{customer_name}"')
def step_impl(context, customer_name):
    customer = parabank.register_customer()
    context.customers = {customer_name: customer}


@then('"{customer_name}" customer data matches the response')
def step_impl(context, customer_name):
    login_response = context.customer_login_response
    customer = context.customers[customer_name]

    assert customer.id == str(login_response.id)
    assert customer.first_name == login_response.first_name
    assert customer.last_name == login_response.last_name
    assert customer.address.street == login_response.address.street
    assert customer.address.city == login_response.address.city
    assert customer.address.state == login_response.address.state
    assert customer.address.zip == login_response.address.zip_code
    assert customer.phone == login_response.phone_number
    assert customer.ssn == login_response.ssn
