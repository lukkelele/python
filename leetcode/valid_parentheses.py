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
        first_char = s[index]
        second_char = s[index+1]
        chars = first_char + second_char
        if len_s == 2:
            if s == "()" or s == "[]" or s == "{}":
                return True
            else: return False
        elif chars == "()" or chars == "[]" or chars == "{}":
            while index < end:
                print(f"len_s == 2  |  s[index]: {s[index]}\ns[index+1]: {s[index+1]}")
                first_char = s[index]
                second_char = s[index+1]
                chars = first_char + second_char
                print(f"chars ==> {chars}")
                if chars == "()" or chars == "[]" or chars == "{}":
                    index += 2
                    continue
                return False
            return True
        else:
            print("entered lower")
            while index <= half:
                print(f"s[index]: {s[index]}\ns[end-index]: {s[end-index]}")
                print(f"half=={half}")
                char1 = s[index]
                char2 = s[end-index]
                chars = char1 + char2
                if chars == "()" or chars == "[]" or chars == "{}":
                    index += 1
                    continue
                return False
                print(index)
            return True





sol = Solution()


s1 = "()[]{}"
s2 = "{[]}"
s3 = "([)]"
s4 = "({[)"

print(sol.isValid(s4))
