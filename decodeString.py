def decodeString(s: str) -> str:
    stack = []

    for c in s:
        if c != "]":
            stack.append(c)
        else:
            temp = []
            while stack[-1] != "[":
                temp.append(stack.pop())
            temp = temp[::-1]
            stack.pop()
            num = ""
            while stack[-1].isnumeric():
                num += stack.pop()                
                if (stack == []):
                    break            
            stack.extend(temp * int(num[::-1]))
    return "".join(stack)


print(decodeString("100[leetcode]"))
