class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = [[], []]

        for num in set(nums1):
            if num not in nums2:
                answer[0].append(num)

        for num in set(nums2):
            if num not in nums1:
                answer[1].append(num)

        return answer
