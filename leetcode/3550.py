class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        output = -1

        for x in range(len(nums)):
            digit_sum = sum(int(x) for x in str(nums[x]))

            if x == digit_sum:
                output = x
                break

        return output
