from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        for num in nums:
            if num % 3 != 0:
                if (num + 1) % 3 == 0 or (num - 1) % 3 == 0:
                    operations += 1
                    continue

        return operations
