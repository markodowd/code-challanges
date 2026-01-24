class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_digit = sum(int(digit) for digit in str(x))

        if x % sum_digit == 0:
            return sum_digit

        return -1
