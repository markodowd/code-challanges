class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        output = 0

        for i in range(len(nums) - 1):
            if (sum(nums[: i + 1]) - sum(nums[i + 1 :])) % 2 == 0:
                output += 1

        return output
