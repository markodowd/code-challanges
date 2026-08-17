import unittest


class Solution:
    def hasIncreasingArray(self, nums: list[int]) -> bool:
        return all(a < b for a, b in zip(nums, nums[1:]))

    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        loop_end = len(nums) - (k * 2)

        for x in range(loop_end + 1):
            sub_1 = nums[x : x + k]
            sub_2 = nums[x + k : x + (k * 2)]

            if self.hasIncreasingArray(sub_1) and self.hasIncreasingArray(sub_2):
                return True

        return False


class TestHasIncreasingSubarrays(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_example_1(self):
        self.assertEqual(
            self.solver.hasIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3), True
        )

    def test_example_2(self):
        self.assertEqual(
            self.solver.hasIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5), False
        )


if __name__ == "__main__":
    unittest.main()
