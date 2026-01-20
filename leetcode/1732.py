class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        output = 0
        trail = 0

        for num in gain:
            trail += num
            output = max(trail, output)

        return output
