# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        week = 0
        day = 1

        for i in range(1, n + 1):
            total += week + day
            day += 1

            if i % 7 == 0:
                day = 1
                week += 1

        return total
