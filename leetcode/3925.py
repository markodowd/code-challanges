class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        reverse = nums[::-1]

        nums.extend(reverse)

        return nums
