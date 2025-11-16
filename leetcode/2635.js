// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let answer = []

    for (let i = 0; i < arr.length; i++) {
        answer.push(fn(arr[i], i))
    }

    return answer
};
