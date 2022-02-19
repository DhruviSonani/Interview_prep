# Check whether string can be palindrom or not
def check_palindrom(string):
    first_odd = 0
    # Approach 1
    Hashmap = dict()
    for i in string:
        if i in Hashmap:
            Hashmap[i] += 1
        else:
            Hashmap[i] = 1

    for i in Hashmap:
        # temp = string.count(i)
        if Hashmap[i] % 2 != 0:
            if first_odd == 0:
                first_odd = 1
            else:
                return False
    return True

    # Approach 2
    for i in string:
        temp = string.count(i)
        if temp % 2 != 0:
            if first_odd == 0:
                first_odd = 1
            else:
                return False
    return True


string = "dhruvidhruvi"
print(check_palindrom(string))
