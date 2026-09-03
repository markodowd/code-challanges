import unittest


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_len = len(name)
        typed_len = len(typed)
        name_ptr = 0

        for i in range(typed_len):
            typed_val = typed[i]

            if name_ptr < name_len and typed_val == name[name_ptr]:
                name_ptr += 1
            elif name_ptr > 0 and typed_val == name[name_ptr - 1]:
                continue
            else:
                return False

        return name_ptr == name_len


class TestIsLongPressedName(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.isLongPressedName("alex", "aaleex"), True)

    def test_2(self):
        self.assertEqual(self.solver.isLongPressedName("saeed", "ssaaedd"), False)

    def test_3(self):
        self.assertEqual(self.solver.isLongPressedName("alex", "aaleexa"), False)


if __name__ == "__main__":
    unittest.main()
