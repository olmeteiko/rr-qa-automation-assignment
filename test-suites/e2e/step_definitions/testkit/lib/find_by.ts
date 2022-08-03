import 'reflect-metadata';


/**
 * Decorator function that returns an element on the page by the selector.
 */
export function findBy(selector: string) {
    return (target: any, propertyKey: string) => {
        const type = Reflect.getMetadata('design:type', target, propertyKey);
        Object.defineProperty(target, propertyKey, {
            configurable: true,
            enumerable: true,
            get: function() {
                const promise = (this as any).browser.findPageElement(selector);
                return new type(promise, selector);
            },
        });
    };
}