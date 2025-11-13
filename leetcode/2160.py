class Solution:
    def minimumSum(self, num: int) -> int:
        digits = list(map(int, str(num)))
        digits.sort()

        a = int(f"{digits[0]}{digits[2]}")
        b = int(f"{digits[1]}{digits[3]}")

        return a + b
