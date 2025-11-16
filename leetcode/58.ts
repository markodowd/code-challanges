// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

function lengthOfLastWord(s: string): number {
  const wordArray = s.split(' ').filter(Boolean)

  return wordArray[wordArray.length - 1].length
}
