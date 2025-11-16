# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def equalFrequency(self, word: str) -> bool:
        count_dict = {}

        for char in word:
            if char in count_dict:
                count_dict[char] = count_dict[char] + 1
            else:
                count_dict[char] = 1

        max_val = max(count_dict.values())

        highest_keys = [k for k, v in count_dict.items() if v == max_val]

        if len(highest_keys) > 1:
            return False

        min_val = min(count_dict.values())

        if max_val - min_val != 1:
            return False

        return True
