class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        flat = [item for sublist in grid for item in sublist]

        seen = set()
        duplicate = None

        for num in flat:
            if num in seen:
                duplicate = num
            seen.add(num)

        missing = None
        n_squared = len(flat)
        for num in range(1, n_squared + 1):
            if num not in seen:
                missing = num
                break

        return [duplicate, missing]

