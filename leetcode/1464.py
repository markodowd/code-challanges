class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        output = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                val = (nums[i] - 1) * (nums[j] - 1)

                output = max(val, output)

        return output

