class Solution:
    def earliestTime(self, tasks: list[list[int]]) -> int:
        output = float("inf")

        for task in tasks:
            x, y = task

            time = x + y

            output = min(output, time)

        return output

