class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        total = 0

        for index, val in enumerate(nums):
            if index.bit_count() == k:
                total += val

        return total
