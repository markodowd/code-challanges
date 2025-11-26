class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count = 0

        for i in range(0, len(nums) - 2):
            for j in range(1, len(nums) - 1):
                for k in range(2, len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count += 1

        return count
