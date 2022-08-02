from mimesis import Person, Address as FakeAddress
from mimesis.random import Random


class Address:
    street = ""
    city = ""
    state = ""
    zip = ""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @staticmethod
    def fake():
        addr = Address()
        fake_addr = FakeAddress()

        addr.__dict__.update({
            "street": fake_addr.street_name(),
            "city": fake_addr.city(),
            "state": fake_addr.state(),
            "zip": fake_addr.zip_code(),
        })
        return addr


class Customer:
    id = ""
    login = ""
    password = ""
    first_name = ""
    last_name = ""
    phone = ""
    ssn = ""
    address = Address()

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @staticmethod
    def fake():
        fake_person = Person()
        customer = Customer()

        customer.__dict__.update({
            "id": Random().custom_code(),
            "login": fake_person.username(mask='l'),
            "password": fake_person.username(mask='l'),
            "first_name": fake_person.first_name(),
            "last_name": fake_person.last_name(),
            "phone": fake_person.telephone(),
            "ssn": Random().custom_code(),
            "address": Address.fake(),
        })
        return customer
