class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        answer: list[int] = []
        nums.sort()

        for i in range(0, len(nums), 2):
            alice = nums[i]
            bob = nums[i+1]

            answer.append(bob)
            answer.append(alice)

        return answer
