import unittest


class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        max_chairs = 0

        for char in s:
            if char == "E":
                chairs += 1
            else:
                chairs -= 1

            max_chairs = max(chairs, max_chairs)

        return max_chairs


class TestMinimumChairs(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.minimumChairs("EEEEEEE"), 7)

    def test_2(self):
        self.assertEqual(self.solver.minimumChairs("ELELEEL"), 2)

    def test_3(self):
        self.assertEqual(self.solver.minimumChairs("ELEELEELLL"), 3)


if __name__ == "__main__":
    unittest.main()
