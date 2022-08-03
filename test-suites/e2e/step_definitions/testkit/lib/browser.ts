import 'chromedriver';
import {Builder, ThenableWebDriver, By, WebElementPromise} from 'selenium-webdriver';
import {Options as ChromeOptions} from 'selenium-webdriver/chrome';

import {InitiatePage, PageName, Pages, Page} from '../pages';
import {WaitCondition} from './conditions';


/**
 * The list of supported browsers.
 */
const enum BrowserType {
    Chrome = 'chrome'
}

/**
 * Browser class provides a concise abstract adapter over a web-browser.
 */
export class Browser {
    private static instance: Browser;
    private driver: ThenableWebDriver;

    /**
     * Creates a new instance of the Chrome browser designated for the E2E testing.
     * TODO: extend with support for another browsers.
     */
    private constructor(headless: boolean = true) {
        const opts = new ChromeOptions();

        this.driver = new Builder()
            .forBrowser(BrowserType.Chrome)
            .setChromeOptions(headless ? opts.headless() : opts)
            .build();
    }

    public static getInstance(): Browser {
        if (!Browser.instance) {
            Browser.instance = new Browser(false);
        }

        return Browser.instance;
    }

    /**
     * Destroys the instance of the browser instance.
     */
    public async exit() {
        await this.driver.quit();
    }

    /**
     * Performs a navigation to a desired page.
     * Returns an instance of the Page for operations.
     */
    public async navigate(page: PageName): Promise<Page> {
        return await this.driver
            .navigate()
            .to(Pages[page])
            .then(() => InitiatePage(page, this));
    }

    /**
     * Returns an element by its selector.
     */
    public findPageElement(selector: string): WebElementPromise {
        return this.driver.findElement(By.css(selector));
    }

    /**
     * Waits until any of the waiting conditions is satisfied.
     * Usage:
     *     await browser.wait(pageHasLoaded(OverviewPage));
     */
    public async wait(conditions: WaitCondition | WaitCondition[]): Promise<void> {
        const all = (!(conditions instanceof Array)) ? [conditions] : conditions;

        await this.driver.wait(async () => {
            for (const condition of all) {
                try {
                    if (await condition(this)) {
                        return true;
                    }
                } catch (ex) {
                }
            }
        });
    }
}
