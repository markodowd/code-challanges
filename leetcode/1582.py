class Solution:
    def check_distinct_row(self, mat: list[list[int]], row: int, col: int) -> bool:
        for j in range(len(mat[0])):
            if j != col:
                if mat[row][j] == 1:
                    return False
        return True

    def check_distinct_col(self, mat: list[list[int]], row: int, col: int) -> bool:
        for i in range(len(mat)):
            if i != row:
                if mat[i][col] == 1:
                    return False
        return True

    def numSpecial(self, mat: list[list[int]]) -> int:
        count = 0
        rows = len(mat)
        cols = len(mat[0])

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    if self.check_distinct_row(mat, i, j) and self.check_distinct_col(
                        mat, i, j
                    ):
                        count += 1
        return count
