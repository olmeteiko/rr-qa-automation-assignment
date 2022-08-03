import {Page} from './Page';
import {Browser, WebComponent, findBy, elementIsVisible} from '../lib';


export class OverviewPage extends (Page) {
    constructor(browser: Browser) {
        super(browser);
    }


    @findBy('div[ng-app="OverviewAccountsApp"]')
    private OverviewContent: WebComponent;


    public loadCondition() {
        return elementIsVisible(() => this.OverviewContent);
    }
}