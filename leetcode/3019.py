class Solution:
    def countKeyChanges(self, s: str) -> int:
        prev = s[0].lower()
        count = 0

        for char in s.lower():
            if char != prev:
                count += 1
                prev = char

        return count


tester = Solution()

ans_1 = tester.countKeyChanges("aAbBcC")

assert ans_1 == 2
