class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = sum(nums)

        result = [int(d) for n in nums for d in str(n)]

        digit_sum = sum(result)

        return abs(element_sum - digit_sum)
