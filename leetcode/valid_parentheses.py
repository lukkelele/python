#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        len_s = len(s)
        if len_s % 2 != 0:
            return False
        half = (len_s/2) - 1
        end = len_s - 1
        index = 0
        c = 0
        char1 = s[index]
        char2 = s[index+1]
        mirror = [["(", ")"], ["[", "]"], ["{", "}"]]
        if char1 == ")" or char1 == "]" or char1 == "}":
            return False
        while index < end:
            print(f"current index: {index}")


sol = Solution()


s1 = "()[]{}"
s2 = "{[]}"
s3 = "([)]"
s4 = "({[)"

print(sol.isValid(s4))
