class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        smallest = -1

        n = len(s)

        if n == 1:
            return 0

        for i in range(n - 1):
            if s[i] == s[n - i - 1]:
                smallest = i
                break

        return smallest
