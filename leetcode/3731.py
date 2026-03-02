class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        output: list[int] = []

        nums.sort()

        min_num = nums[0]
        max_num = nums[-1]

        for num in range(min_num, max_num):
            if num not in nums:
                output.append(num)

        return output
