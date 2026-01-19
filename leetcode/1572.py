class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        length = len(mat[0])
        output = 0

        for i in range(length):
            output += mat[i][i]

        for i in range(length):
            output += mat[i][length - 1 - i]

        if length % 2 != 0:
            mid = length // 2
            output -= mat[mid][mid]

        return output
