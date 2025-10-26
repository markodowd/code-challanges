from typing import List


class Solution:
    def reverseDegree(self, s: str) -> int:
        nums: List[int] = []

        for idx, char in enumerate(s):
            char_idx = ord(char) - ord("a") + 1
            rev_idx = 27 - char_idx
            rev_product = rev_idx * (idx + 1)

            nums.append(rev_product)

        return sum(nums)
