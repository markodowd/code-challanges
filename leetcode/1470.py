# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_arr = []

        for i in range(0, n):
            shuffled_arr.append(nums[i])
            shuffled_arr.append(nums[n + i])

        return shuffled_arr
