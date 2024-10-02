class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writer = 0

        for reader in range(len(nums)):
            if nums[reader] != val:
                nums[writer] = nums[reader]
                writer += 1

        return writer
