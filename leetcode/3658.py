# Bad performance - answer can just be n itself => n
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0

        odd = True

        for num in range(1, (n * 2) + 1):
            if odd:
                sumOdd += num
                odd = False
            else:
                sumEven += num
                odd = True

        gcd = 1

        for i in range(1, sumOdd + 1):
            if sumOdd % i == 0 and sumEven % i == 0:
                gcd = i

        return gcd
