# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        nums_list = list(map(int, date.split("-")))

        bin_list = list(map(lambda n: bin(n)[2:], nums_list))

        return "-".join(bin_list)
