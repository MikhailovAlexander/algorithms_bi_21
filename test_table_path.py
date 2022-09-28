import unittest

from main import get_min_cost_path, ArgumentException


class TestTablePath(unittest.TestCase):
    def test_none(self):
        self.assertRaisesRegex(ArgumentException,
                               'The price table is not a rectangular matrix '
                               'with float values', get_min_cost_path, None)

    def test_empty(self):
        self.assertRaisesRegex(ArgumentException,
                               'The price table is not a rectangular matrix '
                               'with float values', get_min_cost_path, [])

    def test_str_value(self):
        self.assertRaisesRegex(ArgumentException,
                               'The price table is not a rectangular matrix '
                               'with float values', get_min_cost_path, [['ab']])

    def test_jag(self):
        table = [[1., 2., 3.],
                 [1., 2.]]
        self.assertRaisesRegex(ArgumentException,
                               'The price table is not a rectangular matrix '
                               'with float values', get_min_cost_path, table)

    def test_single(self):
        self.assertEqual(get_min_cost_path([[1.]]),
                         {'cost': 1., 'path': [(0, 0)]})

    def test_double(self):
        table = [[1., 2.],
                 [3., 4.]]
        self.assertEqual(get_min_cost_path(table),
                         {'cost': 7., 'path': [(0, 0), (0, 1), (1, 1)]})

    def test_triple(self):
        table = [[1., 2., 2.],
                 [3., 4., 2.],
                 [1., 1., 2.]]
        self.assertEqual(get_min_cost_path(table),
                         {'cost': 8., 'path': [(0, 0), (1, 0), (2, 0), (2, 1),
                                               (2, 2)]})

    def test_rectangle(self):
        table = [[1., 2., 2.],
                 [3., 4., 1.]]
        self.assertEqual(get_min_cost_path(table),
                         {'cost': 6., 'path': [(0, 0), (0, 1), (0, 2), (1, 2)]})

    def test_square(self):
        table = [[1., 2., 2., 1., 3., 4.],
                 [3., 1., 1., 5., 7., 6.],
                 [3., 4., 1., 2., 7., 6.],
                 [5., 7., 1., 6., 4., 4.],
                 [5., 9., 2., 3., 5., 8.],
                 [2., 2., 1., 3., 1., 6.]]
        self.assertEqual(get_min_cost_path(table),
                         {'cost': 20., 'path': [(0, 0), (0, 1), (1, 1), (1, 2),
                                                (2, 2), (3, 2), (4, 2), (5, 2),
                                                (5, 3), (5, 4), (5, 5)]})

    def test_rectangle_large(self):
        table = [[8., 9., 2., 1., 6., 9.],
                 [2., 3., 4., 8., 5., 1.],
                 [4., 1., 7., 7., 1., 7.],
                 [5., 6., 2., 8., 5., 6.],
                 [3., 5., 2., 5., 8., 3.],
                 [6., 9., 1., 3., 1., 5.],
                 [7., 5., 4., 4., 2., 9.],
                 [8., 7., 4., 1., 3., 5.],
                 [6., 5., 7., 7., 6., 2.],
                 [6., 2., 4., 8., 6., 3.],
                 [7., 7., 2., 4., 5., 7.],
                 [3., 8., 1., 6., 7., 1.]]
        self.assertEqual(get_min_cost_path(table),
                         {'cost': 52., 'path': [(0, 0), (1, 0), (1, 1), (2, 1),
                                                (3, 1), (3, 2), (4, 2), (5, 2),
                                                (5, 3), (5, 4), (6, 4), (7, 4),
                                                (7, 5), (8, 5), (9, 5), (10, 5),
                                                (11, 5)]})


if __name__ == '__main__':
    unittest.main()
