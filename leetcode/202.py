class Solution:
    SQUARE_MAP = {str(d): d**2 for d in range(10)}

    def calculateSquareDigits(self, n: int) -> int:
        return sum(self.SQUARE_MAP[x] for x in str(n))

    def isHappy(self, n: int) -> bool:
        num = n
        calculated = set()

        while num != 1:
            num = self.calculateSquareDigits(num)

            if num in calculated:
                return False

            calculated.add(num)

        return True
