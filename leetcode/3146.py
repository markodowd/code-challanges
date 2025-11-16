# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0

        for i in range(len(s)):
            total += abs(i - t.index(s[i]))

        return total
