# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []

        for i, _ in enumerate(nums):
            count = 0

            for j, _ in enumerate(nums):
                if i == j:
                    continue

                if nums[i] > nums[j]:
                    count += 1

            result.append(count)

        return result
