import unittest
from lcs_solver import create_table
from reconstruct import get_lcs
from brute_force import brute_force_lcs, is_subsequence


class TestLCS(unittest.TestCase):

    def check(self, x, y, expected):
        dp = create_table(x, y)
        lcs, path, matches = get_lcs(dp, x, y)
        self.assertEqual(dp[len(x)][len(y)], expected)
        self.assertEqual(len(lcs), expected)
        self.assertTrue(is_subsequence(lcs, x))
        self.assertTrue(is_subsequence(lcs, y))
        self.assertEqual(brute_force_lcs(x, y), expected)
        self.assertEqual(path[0], (len(x), len(y)))
        i, j = path[-1]
        self.assertTrue(i == 0 or j == 0)

    def test_known(self):
        self.check("CBABDAB", "BDCABA", 4)

    def test_identical(self):
        self.check("ABC", "ABC", 3)

    def test_no_common(self):
        self.check("ABC", "XYZ", 0)

    def test_repeated(self):
        self.check("AAAAA", "AA", 2)

    def test_empty(self):
        self.check("", "ABC", 0)


if __name__ == "__main__":
    unittest.main()
