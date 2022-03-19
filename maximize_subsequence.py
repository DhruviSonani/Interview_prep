def maximum(text, pattern):
    ans, ans1 = 0,0
    f = pattern[0]+text
    s = text+pattern[1]
    cnt1 = 0
    for i in range(len(f)):
        # check and increment pattern[0] with text char 
        if f[i] == pattern[0]:
            cnt +=1
        # if pattern[1] then add count to ans
        elif(f[i] == pattern[1]):
            ans+= cnt

# Pattern[0] and pattern[1] is same           
    if pattern[0] == pattern[1]:
        ans = ((cnt1)*(cnt-1))/2
    cnt1 = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == pattern[1]:
            cnt1 += 1
        elif(s[i] == pattern[0]):
            ans1 += cnt1
# Pattern[0] and pattern[1] is same
    if pattern[0] == pattern[1]:
        ans1 = ((cnt1)*(cnt-1))/2

    return int(max(ans, ans1))

text, pat = "aaaab", "aa"
print(maximum(text, pat))