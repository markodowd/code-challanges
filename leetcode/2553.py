class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        answer = ""

        for num in nums:
            answer += str(num)

        return [int(char) for char in answer]
