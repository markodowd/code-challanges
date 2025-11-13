from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1

        return max(count, key=count.get)
