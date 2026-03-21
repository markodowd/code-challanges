class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        before = []
        middle = []
        after = []

        for num in nums:
            if num < pivot:
                before.append(num)
            if num > pivot:
                after.append(num)
            if num == pivot:
                middle.append(num)

        return before + middle + after
