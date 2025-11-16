// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

// dynamic programming approach
// https://youtu.be/Y0lT9Fck7qI?si=EpcoJAdV9KDEGoQB
function climbStairs(n: number): number {
  let one = 1
  let two = 1

  for (let i = 0; i < n - 1; i++) {
    const temp = one
    one = one + two
    two = temp
  }

  return one
}
