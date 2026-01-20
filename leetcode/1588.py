class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total = 0
        n = len(arr)
    
        for length in range(1, n + 1, 2):
            for start in range(n - length + 1):
                for i in range(start, start + length):
                    total += arr[i]
    
        return total
