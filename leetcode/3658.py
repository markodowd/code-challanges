class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = n * n
        sum_even = n * n + n

        tracker = n

        while tracker >= 1:
            if sum_odd % tracker == 0 and sum_even % tracker == 0:
                return tracker

            tracker -= 1

        return 1
