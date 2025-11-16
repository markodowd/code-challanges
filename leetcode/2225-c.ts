// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

function findWinners(_) {
  let e = Array(100001).fill(-1)
  for (let l = 0; l < _.length; l++) {
    let t = _[l][0],
      n = _[l][1]
    ;-1 == e[t] && (e[t] = 0), -1 == e[n] ? (e[n] = 1) : (e[n] = e[n] + 1)
  }
  let $ = [],
    f = []
  for (let r = 1; r < e.length; r++)
    0 === e[r] ? $.push(r) : 1 === e[r] && f.push(r)
  return [$, f]
}
