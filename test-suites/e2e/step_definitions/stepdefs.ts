import {Given, When, Then} from '@cucumber/cucumber';
import {Builder, By, Capabilities, Key} from 'selenium-webdriver';

// driver setup
const capabilities = Capabilities.chrome();
capabilities.set('chromeOptions', {'w3c': false});
const driver = new Builder().withCapabilities(capabilities).build();

Given(/^today is Sunday$/, {timeout: 2 * 5000}, async function () {
    await driver.get('https://parabank.parasoft.com/parabank/index.htm');
    await driver.findElement(By.xpath(`//form/div[@class="login"]/input[@name="username"]`)).sendKeys('john');
    await driver.findElement(By.xpath(`//form/div[@class="login"]/input[@name="password"]`)).sendKeys('demo');
    await driver.findElement(By.xpath(`//form`)).submit();
});

When(/^I ask whether it's Friday yet$/, async function () {

});

Then(/^I should be told "([^"]*)"$/, function (we) {

});
