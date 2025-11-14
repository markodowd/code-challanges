"""
Author: Mark O'Dowd
Email: contact@markodowd.dev
LeetCode: https://leetcode.com/u/markodowd
"""

class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        total_good_pairs = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    total_good_pairs += 1

        return total_good_pairs
