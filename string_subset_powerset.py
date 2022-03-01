def powerSet(string):
    res = [""]
    for i in string:
        res += ["".join(lst) + i for lst in res]
    return res


s = 'abc'
print(powerSet(s))
