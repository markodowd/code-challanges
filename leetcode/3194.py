class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        averages: list[float] = []

        while len(nums) > 0:
            min_val = min(nums)
            max_val = max(nums)

            nums.remove(min_val)
            nums.remove(max_val)

            averages.append((min_val + max_val) / 2)

        return min(averages)
