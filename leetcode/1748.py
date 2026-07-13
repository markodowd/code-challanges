class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        track = {}

        for num in nums:
            track[num] = track.get(num, 0) + 1

        total_sum = 0

        for num, val in track.items():
            if val == 1:
                total_sum += num

        return total_sum
