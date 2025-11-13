from typing import List


class Solution:
    def pascal_row(self, n: int) -> List[int]:
        row = [1]

        for k in range(1, n + 1):
            next_val = row[-1] * (n - k + 1) // k
            row.append(next_val)

        return row

    def generate(self, numRows: int) -> List[List[int]]:
        answer = []

        for num in range(numRows):
            answer.append(self.pascal_row(num))

        return answer
