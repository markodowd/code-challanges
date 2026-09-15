from collections import deque
import unittest


class Solution:
    def lastVisitedIntegers(self, nums: list[int]) -> list[int]:
        seen = deque()
        ans = []
        k = 0

        for i in range(len(nums)):
            value = nums[i]

            if value > 0:
                seen.appendleft(value)
                k = 0

            if value == -1:
                k += 1

                if k <= len(seen):
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)

        return ans


class TestLastVisitedIntegers(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(
            self.solver.lastVisitedIntegers([1, 2, -1, -1, -1]), [2, 1, -1]
        )

    def test_2(self):
        self.assertEqual(self.solver.lastVisitedIntegers([1, -1, 2, -1, -1]), [1, 2, 1])


if __name__ == "__main__":
    unittest.main()
