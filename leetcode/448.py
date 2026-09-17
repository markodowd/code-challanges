import unittest


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums_len = len(nums)

        tracker = {i: 0 for i in range(1, nums_len + 1)}

        for num in nums:
            tracker[num] += 1

        answer = [key for key, value in tracker.items() if value == 0]

        return answer


class TestFindDisappearedNumbers(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(
            self.solver.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6]
        )

    def test_2(self):
        self.assertEqual(self.solver.findDisappearedNumbers([1, 1]), [2])


if __name__ == "__main__":
    unittest.main()
