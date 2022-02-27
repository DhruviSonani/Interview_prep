def isInterleave(s1, s2, s3):
    # https://www.youtube.com/watch?v=ih2OZ9-M3OM
    if len(s1)+len(s2) != len(s3):
        return False

    i = 0
    T = [[False]*(len(s2) + 1)] * (len(s1) + 1)

    if(set.union(set(s1), set(s2)) == set(s3)):
        for i in range(len(T)):
            for j in range(len(T[i])):
                l = i+j-1
                if i == 0 and j == 0:
                    T[i][j] = True
                elif i == 0:
                    if s3[l] == s2[j-1]:
                        T[i][j] = T[i][j-1]
                elif j == 0:
                    if s1[i-1] == s3[l]:
                        T[i][j] = T[i-1][j]
                else:
                    T[i][j] = (T[i-1][j] if s1[i-1] == s3[l]
                               else False) or (T[i][j-1] if s2[j-1] == s3[l] else False)

        return T[len(s1)][len(s2)]
    return False


s1 = "a"
s2 = ""
s3 = "c"
print(isInterleave(s1, s2, s3))
