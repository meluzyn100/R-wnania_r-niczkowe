import unittest
from src.lin_model import f

class TestFunctionF(unittest.TestCase):
    def test_f_zero_denominator(self):
        t = 1
        a = 2
        b = 3
        c = 4
        d = -3  # b + d = 0
        with self.assertRaises(ValueError):
            f(t, a, b, c, d)

    def test_f_specific_case_1(self):
        t = 1
        a = 2
        b = 3
        c = 4
        d = 5
        result = f(t, a, b, c, d)
        expected_result = 0.7504193282848781
        self.assertAlmostEqual(result, expected_result, places=3)

    def test_f_specific_case_2(self):
        t = 0
        a = 1
        b = 2
        c = 3
        d = 4
        result = f(t, a, b, c, d)
        expected_result = 2
        self.assertAlmostEqual(result, expected_result, places=3)

if __name__ == "__main__":
    unittest.main()