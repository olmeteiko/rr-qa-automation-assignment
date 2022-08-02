from behave import *
from testkit.model.customer import Customer


@when('"{customer_name}" logs in with an incorrect "{altered_field}"')
def step_impl(context, customer_name, altered_field):
    # Mutate the customer's field
    customer = context.customers[customer_name]
    setattr(customer, altered_field, getattr(Customer.fake(), altered_field))
    context.customers[customer_name] = customer

    # TODO: This recommended way of executing a step is brittle to the feature alternation.
    context.execute_steps(u'''When "%s" logs in''' % customer_name)
