class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        answer = []

        for i in range(len(matrix)):
            answer.append(sum(matrix[i]))

        return answer
