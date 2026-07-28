class Solution:
    def findGCD(self, nums: list[int]) -> int:
        low = min(nums)
        high = max(nums)

        output = low

        for i in range(1, low + 1):
            if low % i == 0 and high % i == 0:
                output = i

        return output
