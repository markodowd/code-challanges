class Solution:
    def convert_to_base(self, n: int, base: int) -> str:
        if n == 0:
            return "0"

        digits: list[str] = []

        while n > 0:
            digits.append(str(n % base))
            n //= base

        return "".join(reversed(digits))

    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            base_str = self.convert_to_base(n, i)

            if base_str != base_str[::-1]:
                return False

        return True
