// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

function uniqueOccurrences(arr: number[]): boolean {
  const map = new Map<number, number>()

  // Count the number of occurrences of each value
  for (const num of arr) {
    map.set(num, (map.get(num) || 0) + 1)
  }

  // Remove duplicate values
  const set = new Set(map.values())

  // If the size of the set is different from the size of the map, it means that there was a duplicate value
  if (set.size !== map.size) {
    return false
  }

  return true
}
