class Solution:
    def evenNumberBitwiseORs(self, nums: list[int]) -> int:
        output = 0

        for num in nums:
            if num % 2 == 0:
                output |= num

        return output
