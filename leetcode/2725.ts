type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Fn = (...args: JSONValue[]) => void

function cancellable(fn: Fn, args: JSONValue[], t: number): Function {
    fn(...args);
    
    const intervalId = setInterval(() => {
        fn(...args);
    }, t);
    
    const cancelFn = () => {
        clearInterval(intervalId);
    };
    
    return cancelFn;  
};
