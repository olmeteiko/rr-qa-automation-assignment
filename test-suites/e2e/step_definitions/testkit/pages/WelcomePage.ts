import {Page} from './Page';
import {Browser, findBy, elementIsVisible, WebComponent} from '../lib';


export class WelcomePage extends (Page) {
    constructor(browser: Browser) {
        super(browser);
    }


    @findBy('h1.title')
    private WelcomeMessage: WebComponent;


    public loadCondition() {
        return elementIsVisible(() => this.WelcomeMessage);
    }
}