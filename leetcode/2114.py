# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sentence.split(" ")) for sentence in sentences)
