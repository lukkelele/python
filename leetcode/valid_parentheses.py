#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack open brackets
        brackets = ["(", "[", "{", ")", "]", "}"]
        closing = [")", "]", "}"]
        opening = ["(", "[", "{"]
        len_s = len(s)
        half = (len_s/2) - 1
        end = len_s - 1
        stack = []
        if len_s % 2 != 0:
            return False
        for closing_bracket in closing:
            if s[0] == closing_bracket: return False
        for opening_bracket in opening:
            if s[end] == opening_bracket: return False
        for c in s:
            for bracket in brackets:
                if c == "(" or c == "[" or c == "{": stack.append(c) 
                elif c == ")":
                    if stack[(len(stack)-1)] == "(": stack.pop(len(stack)-1)
                    else: return False
                elif c == "]":
                    if stack[(len(stack)-1)] == "[": stack.pop(len(stack)-1)
                    else: return False
                elif c == "}":
                    if stack[(len(stack)-1)] == "{": stack.pop(len(stack)-1)
                    else: return False
        if len(stack) > 0: return False
        else: return True



sol = Solution()

s1 = "()[]{}"
s2 = "{[]}"
s3 = "([)]"
s4 = "({[)"

print(sol.isValid(s1))
