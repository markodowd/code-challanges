// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    let filteredArr: number[] = []

    for (let i = 0; i < arr.length; i++){
        const val = fn(arr[i], i)

        if (val) {
            filteredArr.push(arr[i])
        }
    }

    return filteredArr
};
