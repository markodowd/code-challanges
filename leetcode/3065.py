# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0

        for val in nums:
            if val >= k:
                count += 1
        
        return len(nums) - count
