class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = 0

        while x > 0 or y > 0:
            lsb_a = x & 1
            lsb_b = y & 1

            if lsb_a != lsb_b:
                hamming_distance += 1

            x >>= 1
            y >>= 1

        return hamming_distance
