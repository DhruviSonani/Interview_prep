def wordBreak(s, wordDict):
    ok = [True]
    wordDict = set(wordDict)
    for i in range(1, len(s)+1):
        # for j in range(i):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i))
    return ok[-1]


# print(ok, ok[j], j, ok[j], s[j:i])
# d = set(wordDict)
# # d = wordDict
# length = len(s)
# dp = [False for _ in range(length+1)]
# dp[0] = True
# for start in range(length):
#     if not dp[start]:
#         continue
#     for end in range(start+1, length+1):
#         if s[start: end] in d:
#             dp[end] = True
# return dp[-1]
s, wordDict = "bb", ["a", "b", "bbb", "bbbb"]
print(wordBreak(s, wordDict))
