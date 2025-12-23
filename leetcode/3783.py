class Solution:
    def reverse(self, n: int) -> int:
        return int(str(n)[::-1])

    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.reverse(n))
