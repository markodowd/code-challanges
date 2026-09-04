import unittest


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        for i in range(len(nums)): # Time: O(N) total | Space: O(1) - Loop runs N times
            score = max(nums[0 : i + 1]) - min(nums[i:]) # Time: O(N) per iteration | Space: O(N) per iteration (due to list slicing)

            if score <= k:
                return i

        return -1


class TestFirstStableIndex(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.firstStableIndex([5, 0, 1, 4], 3), 3)

    def test_2(self):
        self.assertEqual(self.solver.firstStableIndex([3, 2, 1], 1), -1)

    def test_3(self):
        self.assertEqual(self.solver.firstStableIndex([0], 0), 0)


if __name__ == "__main__":
    unittest.main()
