from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        largest = 0

        for i in range(len(points) - 1):
            difference = points[i + 1][0] - points[i][0]

            if difference > largest:
                largest = difference

        return largest
