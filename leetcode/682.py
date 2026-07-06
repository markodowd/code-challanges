class Solution:
    def calPoints(self, operations: list[str]) -> int:
        track = []

        for op in operations:
            match op:
                case "+":
                    track.append(track[-1] + track[-2])
                case "D":
                    track.append(track[-1] * 2)
                case "C":
                    track.pop()
                case _:
                    track.append(int(op))

        return sum(track)
