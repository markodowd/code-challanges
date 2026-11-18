class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        count = 1
        length = 0
        score = nums[0] + nums[1]

        nums_len = len(nums)

        if nums_len % 2 != 0:
            length = nums_len - 1
        else:
            length = nums_len

        for i in range(2, length, 2):
            if (nums[i] + nums[i + 1]) == score:
                count += 1

        return count
