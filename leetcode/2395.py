import unittest


class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if (nums[i] + nums[i + 1]) == (nums[j] + nums[j + 1]):
                    return True

        return False


class TestFindSubarrays(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.findSubarrays([4, 2, 4]), True)

    def test_2(self):
        self.assertEqual(self.solver.findSubarrays([1, 2, 3, 4, 5]), False)

    def test_3(self):
        self.assertEqual(self.solver.findSubarrays([0, 0, 0]), True)


if __name__ == "__main__":
    unittest.main()
