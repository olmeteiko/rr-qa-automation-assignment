import {Browser, WaitCondition} from '../lib';


export interface NewablePage<T extends Page> {
    new(browser: Browser): T;
}


export abstract class Page {
    public constructor(protected browser: Browser) {
    }

    public abstract loadCondition(): WaitCondition;
}