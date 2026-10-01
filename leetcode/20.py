import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


class TestIsValid(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.isValid("()"), True)

    def test_2(self):
        self.assertEqual(self.solver.isValid("()[]{}"), True)

    def test_3(self):
        self.assertEqual(self.solver.isValid("(]"), False)

    def test_4(self):
        self.assertEqual(self.solver.isValid("([])"), True)

    def test_5(self):
        self.assertEqual(self.solver.isValid("]"), False)


if __name__ == "__main__":
    unittest.main()
