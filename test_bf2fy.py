import unittest

from bf2fy import get_brackets_pairs

class TestBf2Fy(unittest.TestCase):

    def test_get_brackets_pairs_not_nested(self):
        bf_code = '[][][]'

        self.assertSetEqual(set(get_brackets_pairs(bf_code)), {(0, 1), (2, 3), (4, 5)})

    def test_get_brackets_pairs_nested(self):
        bf_code = '[[[]]]'

        self.assertSetEqual(set(get_brackets_pairs(bf_code)), {(0, 5), (1, 4), (2, 3)})

    def test_get_brackets_pairs_complex(self):
        bf_code = '[[[0]][1]2[[[]]4[]]8]9'

        self.assertSetEqual(set(get_brackets_pairs(bf_code)), {(0, 20), (1, 5), (2, 4), (6, 8), (10, 18), (11, 14), (12, 13), (16, 17)})


if __name__ == '__main__':
    unittest.main()
