# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

from typing import List


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums: List[int] = []

        for i in range(n):
            nums.append(start + 2 * i)
        
        result = 0

        for n in nums:
            result ^= n

        return result
