class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for val in bin(n)[2:]:
            if val == "1":
                count += 1

        return count
