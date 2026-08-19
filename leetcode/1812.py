import unittest


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter_map = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4,
            "e": 5,
            "f": 6,
            "g": 7,
            "h": 8,
        }

        total = letter_map[coordinates[0]] + int(coordinates[1])

        if total % 2 == 0:
            return False
        else:
            return True


class TestSquareIsWhite(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.squareIsWhite("a1"), False)

    def test_a1(self):
        self.assertEqual(self.solver.squareIsWhite("a1"), False)

    def test_a2(self):
        self.assertEqual(self.solver.squareIsWhite("a2"), True)

    def test_a3(self):
        self.assertEqual(self.solver.squareIsWhite("a3"), False)

    def test_a4(self):
        self.assertEqual(self.solver.squareIsWhite("a4"), True)

    def test_a5(self):
        self.assertEqual(self.solver.squareIsWhite("a5"), False)

    def test_a6(self):
        self.assertEqual(self.solver.squareIsWhite("a6"), True)

    def test_a7(self):
        self.assertEqual(self.solver.squareIsWhite("a7"), False)

    def test_a8(self):
        self.assertEqual(self.solver.squareIsWhite("a8"), True)

    def test_b1(self):
        self.assertEqual(self.solver.squareIsWhite("b1"), True)

    def test_b2(self):
        self.assertEqual(self.solver.squareIsWhite("b2"), False)

    def test_b3(self):
        self.assertEqual(self.solver.squareIsWhite("b3"), True)

    def test_b4(self):
        self.assertEqual(self.solver.squareIsWhite("b4"), False)

    def test_b5(self):
        self.assertEqual(self.solver.squareIsWhite("b5"), True)

    def test_b6(self):
        self.assertEqual(self.solver.squareIsWhite("b6"), False)

    def test_b7(self):
        self.assertEqual(self.solver.squareIsWhite("b7"), True)

    def test_b8(self):
        self.assertEqual(self.solver.squareIsWhite("b8"), False)

    def test_c1(self):
        self.assertEqual(self.solver.squareIsWhite("c1"), False)

    def test_c2(self):
        self.assertEqual(self.solver.squareIsWhite("c2"), True)

    def test_c3(self):
        self.assertEqual(self.solver.squareIsWhite("c3"), False)

    def test_c4(self):
        self.assertEqual(self.solver.squareIsWhite("c4"), True)

    def test_c5(self):
        self.assertEqual(self.solver.squareIsWhite("c5"), False)

    def test_c6(self):
        self.assertEqual(self.solver.squareIsWhite("c6"), True)

    def test_c7(self):
        self.assertEqual(self.solver.squareIsWhite("c7"), False)

    def test_c8(self):
        self.assertEqual(self.solver.squareIsWhite("c8"), True)

    def test_d1(self):
        self.assertEqual(self.solver.squareIsWhite("d1"), True)

    def test_d2(self):
        self.assertEqual(self.solver.squareIsWhite("d2"), False)

    def test_d3(self):
        self.assertEqual(self.solver.squareIsWhite("d3"), True)

    def test_d4(self):
        self.assertEqual(self.solver.squareIsWhite("d4"), False)

    def test_d5(self):
        self.assertEqual(self.solver.squareIsWhite("d5"), True)

    def test_d6(self):
        self.assertEqual(self.solver.squareIsWhite("d6"), False)

    def test_d7(self):
        self.assertEqual(self.solver.squareIsWhite("d7"), True)

    def test_d8(self):
        self.assertEqual(self.solver.squareIsWhite("d8"), False)

    def test_e1(self):
        self.assertEqual(self.solver.squareIsWhite("e1"), False)

    def test_e2(self):
        self.assertEqual(self.solver.squareIsWhite("e2"), True)

    def test_e3(self):
        self.assertEqual(self.solver.squareIsWhite("e3"), False)

    def test_e4(self):
        self.assertEqual(self.solver.squareIsWhite("e4"), True)

    def test_e5(self):
        self.assertEqual(self.solver.squareIsWhite("e5"), False)

    def test_e6(self):
        self.assertEqual(self.solver.squareIsWhite("e6"), True)

    def test_e7(self):
        self.assertEqual(self.solver.squareIsWhite("e7"), False)

    def test_e8(self):
        self.assertEqual(self.solver.squareIsWhite("e8"), True)

    def test_f1(self):
        self.assertEqual(self.solver.squareIsWhite("f1"), True)

    def test_f2(self):
        self.assertEqual(self.solver.squareIsWhite("f2"), False)

    def test_f3(self):
        self.assertEqual(self.solver.squareIsWhite("f3"), True)

    def test_f4(self):
        self.assertEqual(self.solver.squareIsWhite("f4"), False)

    def test_f5(self):
        self.assertEqual(self.solver.squareIsWhite("f5"), True)

    def test_f6(self):
        self.assertEqual(self.solver.squareIsWhite("f6"), False)

    def test_f7(self):
        self.assertEqual(self.solver.squareIsWhite("f7"), True)

    def test_f8(self):
        self.assertEqual(self.solver.squareIsWhite("f8"), False)

    def test_g1(self):
        self.assertEqual(self.solver.squareIsWhite("g1"), False)

    def test_g2(self):
        self.assertEqual(self.solver.squareIsWhite("g2"), True)

    def test_g3(self):
        self.assertEqual(self.solver.squareIsWhite("g3"), False)

    def test_g4(self):
        self.assertEqual(self.solver.squareIsWhite("g4"), True)

    def test_g5(self):
        self.assertEqual(self.solver.squareIsWhite("g5"), False)

    def test_g6(self):
        self.assertEqual(self.solver.squareIsWhite("g6"), True)

    def test_g7(self):
        self.assertEqual(self.solver.squareIsWhite("g7"), False)

    def test_g8(self):
        self.assertEqual(self.solver.squareIsWhite("g8"), True)

    def test_h1(self):
        self.assertEqual(self.solver.squareIsWhite("h1"), True)

    def test_h2(self):
        self.assertEqual(self.solver.squareIsWhite("h2"), False)

    def test_h3(self):
        self.assertEqual(self.solver.squareIsWhite("h3"), True)

    def test_h4(self):
        self.assertEqual(self.solver.squareIsWhite("h4"), False)

    def test_h5(self):
        self.assertEqual(self.solver.squareIsWhite("h5"), True)

    def test_h6(self):
        self.assertEqual(self.solver.squareIsWhite("h6"), False)

    def test_h7(self):
        self.assertEqual(self.solver.squareIsWhite("h7"), True)

    def test_h8(self):
        self.assertEqual(self.solver.squareIsWhite("h8"), False)


if __name__ == "__main__":
    unittest.main()
