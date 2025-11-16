// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

type F = (x: number) => number;

function compose(functions: F[]): F {
    if (functions.length === 0) {
        return x => x;
    }

    return function(x) {
        return functions.reduceRight((acc, fn) => fn(acc), x);
    }
};
