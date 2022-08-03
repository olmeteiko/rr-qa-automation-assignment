import {Given, When, AfterAll} from '@cucumber/cucumber';

import {RegisterPage, WelcomePage, OpenAccountPage} from './testkit/pages';
import {Browser, pageHasLoaded} from './testkit/lib';
import {Customer} from './testkit/models';

const browser = Browser.getInstance();


// TODO: Wrap the steps context into an adapter.
Given('a new customer, {string}', function (customerName: string) {
    this.customers = {};
    this.customers[customerName] = Customer.getFake()
});

Given('{string} registers', async function (customerName: string) {
    const registerPage =  await browser.navigate("Register") as RegisterPage;
    await registerPage.fillInCustomerData(this.customers[customerName]);
    await registerPage.submitRegistrationForm();

    await browser.wait(pageHasLoaded(WelcomePage));
});

When('{string} registers a new {string} account', async function (customerName: string, accountType: string) {
    const newAccountPage =  await browser.navigate("OpenAccount") as OpenAccountPage;
    // The rest of the implementation will follow...
});

AfterAll(async function () {
    await browser.exit();
});
