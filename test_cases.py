import unittest
from itertools import combinations
from lcs_solver import create_table
from reconstruct import get_lcs

def subsequences(s, t):
   it = iter(t)
   return all(c in it for c in s)

def brute_force_length(x, y):
    for size in range(len(x), -1, -1):
        for combo in combinations(x, size):
            if subsequences(combo, y):
                return size
    return 0

class TestLCS(unittest.TestCase):
    
    def check(self, x, y, expected):
        dp = create_table(x, y)
        lcs, path = get_lcs(dp, x, y)
        self.assertEqual(dp[len(x)][len(y)], expected)
        self.assertEqual(len(lcs), expected)
        self.assertTrue(subsequences(lcs, x))
        self.assertTrue(subsequences(lcs, y))
        self.assertEqual(brute_force_length(x, y), expected)
        self.assertEqual(path[0], (len(x), len(y)))
        
        i, j = path[-1]
        self.assertTrue(i == 0 or j == 0)
        
    def test_known(self):
        self.check("CBABDAB", "BDCABA", 4)
    def test_identical(self):
         self.check("ABC", "ABC", 3)
    def test_non_common(self):
        self.check("ABC", "XYZ", 0)
    def test_repeated(self):
        self.check("AAAAA", "AA", 2)
    def test_empty(self):
        self.check("", "ABC", 0)
        

if __name__ == "__main__":
    unittest.main()
                        