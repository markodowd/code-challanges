class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        total = nums[0]

        for i in range(1, len(nums)):
            start = max(0, i - nums[i])
            total += sum(nums[start : i + 1])

        return total
