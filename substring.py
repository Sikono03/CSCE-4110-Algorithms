def lcs(x, y):
    w = len(x)
    z =  len(y)
    # create table to store lengths of lcs
    dp = [[0] * (z + 1) for _ in range(w + 1)]
    best = 0
    end_i = 0
    # compare characters of both strings
    for i in range(1, w + 1):
        for j in range(1, z + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > best: # update longest match 
                    best = dp[i][j]
                    end_i = i
    return best, x[end_i - best:end_i] #length and substring