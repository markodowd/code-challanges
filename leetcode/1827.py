class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0
        nums_len = len(nums)

        if nums_len <= 1:
            return operations

        for i in range(nums_len - 1):
            if nums[i] >= nums[i + 1]:
                target_value = nums[i] + 1
                diff = target_value - nums[i + 1]

                operations += diff

                nums[i + 1] = target_value

        return operations
