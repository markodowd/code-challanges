class Solution:
    def isSelfDividing(self, num: int) -> bool:
        for val in str(num):
            int_val = int(val)

            if int_val == 0:
                return False

            if num % int_val != 0:
                return False

        return True

    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        output = []

        for num in range(left, right + 1):
            if self.isSelfDividing(num):
                output.append(num)

        return output
