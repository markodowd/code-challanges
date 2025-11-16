# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for c in columnTitle:
            result = result * 26 + (ord(c) - ord("A") + 1)

        return result
