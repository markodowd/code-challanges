type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type OnceFn = (...args: JSONValue[]) => JSONValue | undefined

function once(fn: Function): OnceFn {
    let calls = 0;

    return function (...args) {
        calls++;

        if (calls > 1) return undefined;

        return fn(...args);    
    };
}
