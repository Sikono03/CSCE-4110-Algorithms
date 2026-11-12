import random
import string
import time
from lcs_solver import create_table


# Time create_table on random strings of each size.
# Returns a list of (n, number of cells, seconds).
def measure(sizes):
    results = []
    for n in sizes:
        x = "".join(random.choices(string.ascii_uppercase, k=n))
        y = "".join(random.choices(string.ascii_uppercase, k=n))
        start = time.perf_counter()
        create_table(x, y)
        seconds = time.perf_counter() - start
        results.append((n, n * n, seconds))
    return results
