import {Browser} from '../lib';
import {Page} from './Page';
import {IndexPage} from './IndexPage';
import {OverviewPage} from './OverviewPage';
import {RegisterPage} from './RegisterPage';
import {OpenAccountPage} from './OpenAccountPage';


const baseUrl = 'https://parabank.parasoft.com/parabank';


/**
 * The list of all the application's pages URLs.
 */
export const Pages = {
    'Index': `${baseUrl}/index.htm`,
    'Overview': `${baseUrl}/overview.htm`,
    'Register': `${baseUrl}/register.htm`,
    'OpenAccount': `${baseUrl}/openaccount.htm`,
}


export type PageName = keyof typeof Pages;


/**
 * Page factory that returns a page instance by its name.
 */
export function InitiatePage(page: PageName, browser: Browser): Page {
    switch (page) {
        case 'Index':
            return new IndexPage(browser);
        case 'Overview':
            return new OverviewPage(browser);
        case 'Register':
            return new RegisterPage(browser);
        case 'OpenAccount':
            return new OpenAccountPage(browser);
    }
}