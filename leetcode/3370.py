# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def smallestNumber(self, n: int) -> int:
        binary_str = "1"

        while int(binary_str, 2) < n:
            binary_str += "1"

        return int(binary_str, 2)
