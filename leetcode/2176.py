class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        output = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if (i * j) % k == 0:
                        output += 1

        return output

