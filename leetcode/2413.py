class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        smallest = 0

        while smallest % 2 != 0 or smallest % n != 0:
            smallest += 1

        return smallest
