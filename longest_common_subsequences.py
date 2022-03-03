from cgitb import text


def longestCommonSubsequence(text1, text2):
    dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]    
    t1 = " " + text1
    t2 = " " + text2

    for i in range(1, len(t1)):
        for j in range(1, len(t2)):
            if t1[i] == t2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


t1,  t2 = "abcba", "abcbcba"

print(longestCommonSubsequence(t1, t2))
