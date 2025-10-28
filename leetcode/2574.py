from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            leftSum = 0
            rightSum = 0

            if i > 0:
                leftSum = sum(nums[:i])

            if i < (len(nums)):
                rightSum = sum(nums[i + 1 :])

            result.append(abs(leftSum - rightSum))

        return result
