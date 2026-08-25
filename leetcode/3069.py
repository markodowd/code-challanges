import unittest


class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        ans_1 = [nums[0]]
        ans_2 = [nums[1]]

        for i in range(2, len(nums)):
            if ans_1[-1] > ans_2[-1]:
                ans_1.append(nums[i])
            else:
                ans_2.append(nums[i])

        return ans_1 + ans_2


class TestResultArray(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.resultArray([2, 1, 3]), [2, 3, 1])

    def test_2(self):
        self.assertEqual(self.solver.resultArray([5, 4, 3, 8]), [5, 3, 4, 8])


if __name__ == "__main__":
    unittest.main()
