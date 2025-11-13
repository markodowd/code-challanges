class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        split = s.split()

        return " ".join(split[:k])
