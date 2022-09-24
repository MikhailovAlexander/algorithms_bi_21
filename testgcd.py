import unittest

from main import gcd_recursive, gcd_iterative_slow, gcd_iterative_fast
from gcd_gen import GcdGenerator


class TestGcd(unittest.TestCase):
    gcd_functions = [gcd_recursive, gcd_iterative_slow, gcd_iterative_fast]

    def test_first_none(self):
        for gcd in self.gcd_functions:
            self.assertRaises(Exception, gcd, None, 1)

    def test_second_none(self):
        for gcd in self.gcd_functions:
            self.assertRaises(Exception, gcd, 1, None)

    def test_simple(self):
        for gcd in self.gcd_functions:
            self.assertEqual(gcd(9, 3), 3)

    def test_simple_long(self):
        for gcd in self.gcd_functions:
            self.assertEqual(gcd(1005002, 1354), 2)

    def test_random(self):
        gcd_gen = GcdGenerator()
        for gcd in self.gcd_functions:
            for i in range(10):
                if gcd == gcd_iterative_fast:
                    gcd_gen.generate_values(9, 5)
                else:
                    gcd_gen.generate_values(3, 2)
                self.assertEqual(gcd(gcd_gen.a_value, gcd_gen.b_value),
                                 gcd_gen.gcd_value)


if __name__ == '__main__':
    unittest.main()
