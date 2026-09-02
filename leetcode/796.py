import unittest


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in (goal + goal)


# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:
#         s_len = len(s)
#
#         if s_len != len(goal):
#             return False
#
#         if s[0] not in goal:
#             return False
#
#         goal_idx = goal.index(s[0])
#
#         for i in range(s_len):
#             if s[i] == goal[goal_idx]:
#                 if goal_idx == s_len - 1:
#                     goal_idx = 0
#                 else:
#                     goal_idx += 1
#             else:
#                 return False
#
#         return True


class TestRotateString(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.rotateString("abcde", "cdeab"), True)

    def test_2(self):
        self.assertEqual(self.solver.rotateString("abcde", "abced"), False)

    def test_3(self):
        self.assertEqual(self.solver.rotateString("uqbjvaxu", "xuuqbjva"), True)


if __name__ == "__main__":
    unittest.main()
