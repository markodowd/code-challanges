# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return self.pascal_row(rowIndex)

    def pascal_row(self, n: int) -> List[int]: 
        row = [1] 
        
        for k in range(1, n + 1): 
            next_val = row[-1] * (n - k + 1) // k
            row.append(next_val) 
        
        return row
