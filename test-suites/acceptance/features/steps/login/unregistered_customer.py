from behave import given
from testkit.model.customer import Customer


@given('an unregistered customer, "{customer_name}"')
def step_impl(context, customer_name):
    context.customers = {customer_name: Customer.fake()}
