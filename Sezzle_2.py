# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    al = []
    rows = S.split("\n")
    finalString = ""
    for i in range(len(rows)):
        al.append(rows[i])

    al = [item for item in al if (not ",NULL," or not "NULL\n" or not ",NULL" in item)]

    for i in range(len(al)):
        finalString += al[i]+"\n"

    ans = finalString[0:len(finalString)-1]
    return ans


S = 'id,name,age,score\n1,Jack,NULL,12\n17,Betty,28,11'
print(solution(S))
