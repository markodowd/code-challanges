class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for row in range(rows):
            for col in range(cols):
                if row > 0:
                    grid[row][col] += grid[row - 1][col]
                if col > 0:
                    grid[row][col] += grid[row][col - 1]
                if row > 0 and col > 0:
                    grid[row][col] -= grid[row - 1][col - 1]

                if grid[row][col] <= k:
                    count += 1
                else:
                    break

        return count
