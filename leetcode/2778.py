class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        total = 0

        nums_len = len(nums)

        for i in range(nums_len):
            if nums_len % (i + 1) == 0:
                total += nums[i] * nums[i]

        return total
