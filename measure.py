import random 
import time
import string
from lcs_solver import create_table

def measure(sizes):
    total = []
    for n in sizes:
        x = ''.join(random.choices(string.ascii_uppercase, k=n))
        y = ''.join(random.choices(string.ascii_uppercase, k=n))
        start_time = time.perf_counter()
        create_table(x, y)
        end_time = time.perf_counter() - start_time
        total.append((n, n * n, end_time))
    return total

