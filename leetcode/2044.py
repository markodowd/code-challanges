class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        n = len(nums)
        target_or = 0
        for x in nums:
            target_or |= x

        count = 0

        for i in range(1, 1 << n):
            current_or = 0
            for j in range(n):
                if (i >> j) & 1:
                    current_or |= nums[j]

            if current_or == target_or:
                count += 1

        return count
