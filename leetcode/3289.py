from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        tracker = {}

        for num in nums:
            if num in tracker:
                tracker[num] = tracker[num] + 1
            else:
                tracker[num] = 1
        
        return [k for k, v in tracker.items() if v == 2]

