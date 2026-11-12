# Letters must be next to each other.
# Returns its length and the substring itself.
def longest_common_substring(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    best = 0
    end_i = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > best:
                    best = dp[i][j]
                    end_i = i
    return best, x[end_i - best:end_i]
