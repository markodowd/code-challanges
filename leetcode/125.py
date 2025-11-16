# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r"[^a-zA-Z0-9]", "", s.lower())

        return cleaned == cleaned[::-1]
