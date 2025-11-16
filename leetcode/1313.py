# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        answer = []

        for i in range(0, len(nums), 2):
            arr = [nums[i+1]] * nums[i]
            answer.extend(arr)

        return answer
