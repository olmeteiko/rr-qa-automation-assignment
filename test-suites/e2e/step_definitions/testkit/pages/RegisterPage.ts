import {Page} from './Page';
import {Browser, WebComponent, findBy, elementIsVisible, TextInput, Button} from '../lib';
import {Customer} from '../models';


export class RegisterPage extends (Page) {
    constructor(browser: Browser) {
        super(browser);
    }


    @findBy('form[id="customerForm"]')
    private CustomerRegistrationForm: WebComponent;

    @findBy('input[type="submit"]')
    private FormSubmitButton: Button;

    @findBy('input[id="customer.firstName"]')
    private FirstName: TextInput;

    @findBy('input[id="customer.lastName"]')
    private LastName: TextInput;

    @findBy('input[id="customer.address.street"]')
    private Street: TextInput;

    @findBy('input[id="customer.address.city"]')
    private City: TextInput;

    @findBy('input[id="customer.address.state"]')
    private State: TextInput;

    @findBy('input[id="customer.address.zipCode"]')
    private Zip: TextInput;

    @findBy('input[id="customer.phoneNumber"]')
    private Phone: TextInput;

    @findBy('input[id="customer.ssn"]')
    private Ssn: TextInput;

    @findBy('input[id="customer.username"]')
    private Username: TextInput;

    @findBy('input[id="customer.password"]')
    private Password: TextInput;

    @findBy('input[id="repeatedPassword"]')
    private RepeatedPassword: TextInput;


    public loadCondition() {
        return elementIsVisible(() => this.CustomerRegistrationForm);
    }

    public async fillInCustomerData(customer: Customer) {
        await this.FirstName.type(customer.firstName);
        await this.LastName.type(customer.lastName);
        await this.Street.type(customer.street);
        await this.City.type(customer.city);
        await this.State.type(customer.state);
        await this.Zip.type(customer.state);
        await this.Phone.type(customer.phone);
        await this.Ssn.type(customer.ssn);
        await this.Username.type(customer.username);
        await this.Password.type(customer.password);
        await this.RepeatedPassword.type(customer.password);
    }

    public async submitRegistrationForm() {
        await this.FormSubmitButton.click();
    }
}