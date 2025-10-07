from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        str_end = len(s)

        for i in range(str_end // 2):
            temp = s[i]
            s[i] = s[str_end - (i+1)]
            s[str_end - (i+1)] = temp

