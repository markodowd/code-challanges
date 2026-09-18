import unittest


class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            found = False

            for nums in ranges:
                if i in range(nums[0], nums[1] + 1):
                    found = True
                    break

            if not found:
                return False

        return True


class TestIsCovered(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.isCovered([[1, 2], [3, 4], [5, 6]], 2, 5), True)

    def test_2(self):
        self.assertEqual(self.solver.isCovered([[1, 10], [10, 20]], 21, 21), False)

    def test_3(self):
        self.assertEqual(self.solver.isCovered([[1, 1]], 1, 50), False)


if __name__ == "__main__":
    unittest.main()
