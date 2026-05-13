class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        total = 0

        nums.sort()

        for i in range(len(nums) - 1, 0, -2):
            x = nums[i]
            y = nums[i - 1]

            total += min(x, y)

        return total
