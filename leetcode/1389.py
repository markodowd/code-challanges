# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = []

        for i in range(len(nums)):
            target.insert(index[i], nums[i])

        return target
        
