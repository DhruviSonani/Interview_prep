class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ")":
                stack.append(i)
            else:
                temp = ""
                while stack != [] and stack[-1] != "(":
                    temp += stack.pop()
                stack.pop()
                stack.append(temp[::-1])
        for i in range(len(stack)):
            stack[i] = stack[i][::-1]
        return "".join(stack)
