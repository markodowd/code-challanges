class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        ans_1 = [nums[0]]
        ans_2 = [nums[1]]

        for i in range(2, len(nums)):
            if ans_1[-1] > ans_2[-1]:
                ans_1.append(nums[i])
            else:
                ans_2.append(nums[i])

        return ans_1 + ans_2
