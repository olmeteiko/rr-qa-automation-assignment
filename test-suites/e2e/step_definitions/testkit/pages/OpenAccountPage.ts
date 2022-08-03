import {Page} from './Page';
import {Browser, findBy, elementIsVisible, WebComponent} from '../lib';


export class OpenAccountPage extends (Page) {
    constructor(browser: Browser) {
        super(browser);
    }


    @findBy('div[ng-app="AddAccountApp"]')
    private OpenAccountComponent: WebComponent;


    public loadCondition() {
        return elementIsVisible(() => this.OpenAccountComponent);
    }
}