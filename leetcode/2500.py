class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        output = 0
        col_len = len(grid)
        row_len = len(grid[0])

        for _ in range(row_len):
            max_in_step = 0

            for col in range(col_len):
                max_row = -1
                max_idx = -1

                for row in range(row_len):
                    if grid[col][row] > max_row:
                        max_row = grid[col][row]
                        max_idx = row

                grid[col][max_idx] = -1

                if max_row > max_in_step:
                    max_in_step = max_row

            output += max_in_step

        return output
