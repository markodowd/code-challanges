# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        grid_len = len(grid)
        answer = []
        temp = []

        for i in range(grid_len - 2):
            temp = []
            for j in range(grid_len - 2):        
                max_val = max(
                    grid[i][j],
                    grid[i+1][j],
                    grid[i+2][j],
                    grid[i][j+1],
                    grid[i+1][j+1],
                    grid[i+2][j+1],
                    grid[i][j+2],
                    grid[i+1][j+2],
                    grid[i+2][j+2],
                )

                temp.append(max_val)

                if len(temp) == grid_len - 2:
                    answer.append(temp)

        return answer
