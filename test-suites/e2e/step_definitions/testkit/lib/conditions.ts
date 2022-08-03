import {Browser} from './browser';
import {WebComponent} from './html_components';
import {NewablePage, Page} from '../pages/Page';

export type WaitCondition = (browser: Browser) => Promise<boolean>;


/**
 * Resolves successfully if an element specified by the locator is displayed on the page.
 */
export function elementIsVisible(locator: () => WebComponent): WaitCondition {
    return async () => await locator().isDisplayed();
}

/**
 * Resolves successfully if an element specified by the locator is present on the page.
 */
export function elementIsPresent(locator: () => WebComponent): WaitCondition {
    return async () => await locator() !== undefined;
}

/**
 * Resolves successfully Page object's load condition is satisfied.
 */
export function pageHasLoaded<T extends Page>(page: NewablePage<T>): WaitCondition {
    return (browser: Browser) => {
        const condition = new page(browser).loadCondition();
        return condition(browser);
    };
}