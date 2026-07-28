class Solution:
    def countOnes(self, bin_str: str) -> int:
        count = 0

        for i in bin_str:
            if i == "1":
                count += 1

        return count

    def countBits(self, n: int) -> list[int]:
        result = []

        for i in range(n + 1):
            binary_string = bin(i)[2:]

            if i > 1:
                result.append(self.countOnes(binary_string))
            else:
                result.append(int(binary_string))

        return result
