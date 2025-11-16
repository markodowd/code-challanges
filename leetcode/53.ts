// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

// Kadane's algorithm - https://youtu.be/5WZl3MMT0Eg

function maxSubArray(nums: number[]): number {
  let max = nums[0] // defaulting to first value in case of single element array but also can't be 0 because of negative numbers
  let sum = 0 // sum of current subarray

  for (const num of nums) {
    // doesn't apply to first element but if the sum drops below 0, it's better to start a new subarray
    if (sum < 0) {
      sum = 0 // reset sum if it's negative
    }

    sum += num // add current number to sum

    max = Math.max(max, sum) // either the just calculated sum is now greater or just keep the previous max
  }

  return max
}
