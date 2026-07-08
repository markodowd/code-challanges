class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [char for char in str(n) if char != "0"]

        if not digits:
            return 0

        total_num = int("".join(digits))
        digit_sum = sum(int(d) for d in digits)

        return total_num * digit_sum
