# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        split = s.split()

        return " ".join(split[:k])
