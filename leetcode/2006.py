class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(1, len(nums) - 1):
                if abs(nums[i] - nums[j]) == k:
                    count += 1

        return count
