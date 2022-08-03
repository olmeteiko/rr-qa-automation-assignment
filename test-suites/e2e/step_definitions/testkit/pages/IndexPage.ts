import {Page} from './Page';
import {Browser, Button, TextInput, findBy, elementIsVisible} from '../lib';


export class IndexPage extends (Page) {
    constructor(browser: Browser) {
        super(browser);
    }


    @findBy('form[name="login"] input[name="username"]')
    private UsernameField: TextInput;

    @findBy('form[name="login"] input[name="password"]')
    private PasswordField: TextInput;

    @findBy('form[name="login"] input[type="submit"]')
    private SubmitButton: Button;


    public loadCondition() {
        return elementIsVisible(() => this.UsernameField);
    }

    public async login(username: string, password: string): Promise<void> {
        await this.UsernameField.type(username);
        await this.PasswordField.type(password);
        await this.SubmitButton.click();
    }
}