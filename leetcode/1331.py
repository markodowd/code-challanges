class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_unique = sorted(set(arr))

        ranks = {num: rank + 1 for rank, num in enumerate(sorted_unique)}

        return [ranks[num] for num in arr]
