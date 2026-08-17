class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        even_count = {}
        max_freq = 0
        result = -1

        for num in nums:
            if num % 2 == 0:
                freq = even_count.get(num, 0) + 1
                even_count[num] = freq

                if freq > max_freq or (
                    freq == max_freq and (result == -1 or num < result)
                ):
                    max_freq = freq
                    result = num

        return result


tester = Solution()

ans = tester.mostFrequentEven([0, 1, 2, 2, 4, 4, 1])
assert ans == 2
