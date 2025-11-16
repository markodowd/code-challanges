// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

const romanValue = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

function romanToInt(s: string): number {
  return s.split("").reduce((total, _, index) => {
    if (romanValue[s[index]] < romanValue[s[index + 1]]) {
      return total - romanValue[s[index]];
    } else {
      return total + romanValue[s[index]];
    }
  }, 0);
}
