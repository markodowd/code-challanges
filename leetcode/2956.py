class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Matches = 0
        nums2Matches = 0

        for value in nums1:
            if value in nums2:
                nums1Matches += 1

        for value in nums2:
            if value in nums1:
                nums2Matches += 1

        return [nums1Matches, nums2Matches]
