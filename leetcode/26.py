# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = 1

        for reader in range(1, len(nums)):
            if nums[reader] != nums[reader - 1]:
                nums[writer] = nums[reader]
                writer += 1

        return writer
