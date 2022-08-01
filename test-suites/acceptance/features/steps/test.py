from behave import *
from swagger_client.api.misc_api import MiscApi


@given('"{a:d}" equals to "{b:d}"')
def step_impl(context, a, b):
    assert a == b