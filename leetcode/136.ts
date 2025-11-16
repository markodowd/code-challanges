// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

function singleNumber(nums: number[]): number {
  //   create map counting number of times each item appeared
  let countMap = nums.reduce((el, idx) => {
    el[idx] = el[idx] ? el[idx] + 1 : 1
    return el
  }, {})

  // find the key with a value of 1 appearance
  return Number(Object.keys(countMap).find((key) => countMap[key] === 1))
}
