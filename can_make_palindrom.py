from dis import code_info
from enum import Flag

# Brute force, will get TLE
def canMakePaliQueries(s, queries):
    ans = []
    for i in queries:
        splitted = s[i[0]:i[1]+1]
        Hashmap = {}
        for k in splitted:
            if k in Hashmap:
                Hashmap[k] += 1
            else:
                Hashmap[k] = 1

        count = 0
        if len(splitted) > 1:
            for h in Hashmap.values():
                if h % 2 != 0:
                    count += 1
        # if count >= 0:
        if count//2 <= i[2]:
                ans.append(True)
        else:
                ans.append(False)
    return ans

# 2923 ms
def canMakePaliQueries_2(s, queries):
        prefix = {}
        length = len(s)
        prefix[0] = {s[0]: 1}

        for i in range(1, length):
            prefix[i] = prefix[i-1].copy()
            if s[i] in prefix[i]:
                prefix[i][s[i]] += 1
            else:
                prefix[i][s[i]] = 1

            res = []

        for q in queries:
            one = 0
            print(q)
            for k in prefix[q[1]]:
                chars = prefix[q[1]][k] - (prefix[q[0]-1].get(k, 0) if q[0] > 0 else 0)
                one += chars % 2
            if one <= 1:
                res.append(True)
            else:
                res.append(q[2] >= (one//2))
        return res


def canMakePaliQueries_optimal(s, queries):
        rec = [0] * 26
        check = [rec.copy()]
        for c in s:
            rec[ord(c) - ord('a')] += 1
            check.append(rec.copy())        
        ans = []
        for l, r, k in queries:
            count = 0
            rr, ll = check[r+1], check[l] 
            print( check[l], check[r])
            for c in range(26):
                count += (rr[c] - ll[c]) % 2
            ans.append(count//2 <=k)


        return ans

s, queries = "abcda",   [[3, 3, 0]]
print(canMakePaliQueries(s, queries))
