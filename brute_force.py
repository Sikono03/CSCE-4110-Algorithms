from itertools import combinations

def subsequences(s, t):
    it = iter(t)
    return all(c in it for c in s)
 
 # Find the length of the longest common subsequence of x and y by brute force.  
def brute_force_lcs(x, y):
    
    for size in range(len(x), -1, -1):
        for combo in combinations(x, size): # subsequences of x
            if subsequences(combo, y): # check if combo is a subsequence of y
                return size
    return 0