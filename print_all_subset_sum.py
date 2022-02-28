def printS(ind, ds, s, sum, arr, n):
    if ind == n:
        if s == sum:
            for i in ds:
                print(i, " ")
            print()
        return

    # Pick element
    ds.append(arr[ind])
    s += arr[ind]
    printS(ind+1, ds, s, sum, arr, n)
    s -= arr[ind]
    ds.pop()

    # Not pick an element
    printS(ind+1, ds, s, sum, arr, n)


arr = [1, 2, 1]
sum = 5
ds = []
printS(0, ds, 0, sum, arr, len(arr))
