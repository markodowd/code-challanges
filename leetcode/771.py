class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0

        for char in stones:
            if char in jewels:
                total += 1

        return total
