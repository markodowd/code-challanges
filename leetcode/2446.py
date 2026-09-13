import unittest


class Solution:
    def to_minutes(self, t: str) -> int:
        hours, minutes = map(int, t.split(":"))

        return (hours * 60) + minutes

    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        start1, end1 = self.to_minutes(event1[0]), self.to_minutes(event1[1])
        start2, end2 = self.to_minutes(event2[0]), self.to_minutes(event2[1])

        return max(start1, start2) <= min(end1, end2)


class TestHaveConflict(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(
            self.solver.haveConflict(["01:15", "02:00"], ["02:00", "03:00"]), True
        )

    def test_2(self):
        self.assertEqual(
            self.solver.haveConflict(["01:00", "02:00"], ["01:20", "03:00"]), True
        )

    def test_3(self):
        self.assertEqual(
            self.solver.haveConflict(["10:00", "11:00"], ["14:00", "15:00"]), False
        )


if __name__ == "__main__":
    unittest.main()
