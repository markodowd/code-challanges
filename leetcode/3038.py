class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        score = nums[0] + nums[1]
        count = 0

        for i in range(0, len(nums) - 1, 2):
            if nums[i] + nums[i + 1] == score:
                count += 1
            else:
                break

        return count
