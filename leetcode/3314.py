class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []

        for num in nums:
            found = False

            for candidate in range(num):
                if candidate | (candidate + 1) == num:
                    ans.append(candidate)
                    found = True
                    break

            if not found:
                ans.append(-1)

        return ans
