class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        str_digits = str(n)

        digit_sum = sum(map(int, str_digits))
        square_sum = sum(int(d) ** 2 for d in str_digits)

        return (square_sum - digit_sum) >= 50
