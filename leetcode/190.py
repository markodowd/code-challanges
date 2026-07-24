class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = format(n, "032b")

        return int(binary_string[::-1], 2)
