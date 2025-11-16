# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []

        max_val = max(candies)

        for kid in candies:
            if kid + extraCandies >= max_val:
                result.append(True)
            else:
                result.append(False)

        return result
