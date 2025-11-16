# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = str(n)

        product = int(digits[0])
        sum_digits = int(digits[0])

        for i in range(1, len(digits)):
            product *= int(digits[i])
            sum_digits += int(digits[i])

        return product - sum_digits
