import {faker} from '@faker-js/faker';

export class Customer {
    public username: string;
    public password: string;

    public firstName: string;
    public lastName: string;
    public street: string;
    public city: string;
    public state: string;
    public zip: string;
    public phone: string;
    public ssn: string;

    /**
     * Returns a model prefilled with fake data.
     */
    public static getFake() {
        const c = new Customer();
        c.username = faker.internet.userName();
        c.password = faker.random.alphaNumeric(10);
        c.firstName = faker.name.firstName();
        c.lastName = faker.name.lastName();
        c.street = faker.address.streetAddress();
        c.city = faker.address.city();
        c.state = faker.address.state();
        c.zip = faker.address.zipCode();
        c.phone = faker.phone.number();
        c.ssn = faker.phone.imei();
        return c;
    }
}