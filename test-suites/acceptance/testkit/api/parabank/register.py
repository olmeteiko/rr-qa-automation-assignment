from testkit.model.customer import Customer, Address


# register_customer registers the customer in the ParaBank Web-Service and returns its DTO.
# Due to the non-existence of the customer creation endpoint at the moment, this function
# exploits the current design and returns the preregistered customer's data.
# TODO: Replace with a call to the ParaBank API when the endpoint is ready.
def register_customer():
    return Customer(id="12212", login="john", password="demo", first_name="John", last_name="Smith",
                    address=Address(street="1431 Main St", city="Beverly Hills", state="CA", zip="90210"),
                    phone="310-447-4121", ssn="622-11-9999")
