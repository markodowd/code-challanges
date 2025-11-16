// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

function findIntersectionValues(nums1: number[], nums2: number[]): number[] {
  let nums1Matches = 0
  let nums2Matches = 0

  for (const value of nums1) {
    if (nums2.includes(value)) {
      nums1Matches++
    }
  }

  for (const value of nums2) {
    if (nums1.includes(value)) {
      nums2Matches++
    }
  }

  return [nums1Matches, nums2Matches]
}
