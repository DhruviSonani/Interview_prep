def printS(ind, ds, s, sum, arr, n):
    if ind == n:
        if s == sum:
            for i in ds:
                print(i, " ")
            print()
            return True
        return False

    # Pick element
    ds.append(arr[ind])
    s += arr[ind]
    if (printS(ind+1, ds, s, sum, arr, n)):
        return True
    s -= arr[ind]
    ds.pop()

    # Not pick an element
    if(printS(ind+1, ds, s, sum, arr, n)):
        return True
    return False


arr = [1, 2, 1]
sum = 2
ds = []
printS(0, ds, 0, sum, arr, len(arr))
