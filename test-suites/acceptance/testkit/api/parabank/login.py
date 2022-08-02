from testkit.model.customer import Customer
from .parabank_swagger_client.api.misc_api import MiscApi
from swagger_client.rest import ApiException
from .errors import ApiError


def login(user: Customer):
    api = MiscApi()
    try:
        return api.login1(user.login, user.password)
    except ApiException as err:
        raise ApiError(err)
