// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

// https://stackoverflow.com/a/1804686
function isPowerOfTwo(n: number): boolean {
  return n !== 0 && n > 0 && (n & (n - 1)) == 0;
}
