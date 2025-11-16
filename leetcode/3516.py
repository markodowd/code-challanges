# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        abs_1 = abs(x - z)
        abs_2 = abs(y - z)

        if abs_1 == abs_2:
            return 0

        if abs_1 > abs_2:
            return 2
        else:
            return 1
