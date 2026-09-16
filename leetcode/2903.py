import unittest


class Solution:
    def findIndices(
        self, nums: list[int], indexDifference: int, valueDifference: int
    ) -> list[int]:
        nums_len = len(nums)
        answer = [-1, -1]

        for i in range(nums_len):
            for j in range(nums_len):
                if (
                    abs(i - j) >= indexDifference
                    and abs(nums[i] - nums[j]) >= valueDifference
                ):
                    return [i, j]

        return answer


class TestFindIndices(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertIn(self.solver.findIndices([5, 1, 4, 1], 2, 4), [[0, 3], [3, 0]])

    def test_2(self):
        self.assertIn(
            self.solver.findIndices([2, 1], 0, 0), [[0, 0], [0, 1], [1, 0], [1, 1]]
        )

    def test_3(self):
        self.assertEqual(self.solver.findIndices([1, 2, 3], 2, 4), [-1, -1])

    def test_4(self):
        self.assertEqual(self.solver.findIndices([0], 0, 0), [0, 0])

    def test_5(self):
        self.assertEqual(self.solver.findIndices([3], 1, 1), [-1, -1])


if __name__ == "__main__":
    unittest.main()
