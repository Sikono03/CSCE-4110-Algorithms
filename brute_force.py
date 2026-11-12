from itertools import combinations


# True if s is a subsequence of t
def is_subsequence(s, t):
    it = iter(t)
    return all(c in it for c in s)


def brute_force_lcs(x, y):
    for size in range(len(x), -1, -1):
        for combo in combinations(x, size):
            if is_subsequence(combo, y):
                return size
    return 0
