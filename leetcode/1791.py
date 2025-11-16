# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        num_1 = edges[0][0]
        num_2 = edges[0][1]
        num_3 = edges[1][0]
        num_4 = edges[1][1]

        if num_3 == num_1 or num_3 == num_2:
            return num_3
        else:
            return num_4
