class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bin_a = bin(start)[2:]
        bin_b = bin(goal)[2:]

        max_len = max(len(bin_a), len(bin_b))

        bin_a = bin_a.zfill(max_len)
        bin_b = bin_b.zfill(max_len)

        changes = 0

        for idx, char in enumerate(bin_a):
            if char != bin_b[idx]:
                changes += 1

        return changes
