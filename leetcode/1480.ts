// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

function runningSum(nums: number[]): number[] {
  let sum = 0

  return nums.map((num) => {
    sum += num
    return sum
  })
}
