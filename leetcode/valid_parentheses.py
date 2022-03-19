#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        closing = [")", "]", "}"]
        brackets = ["(", "[", "{"]
        len_s = len(s)
        if len_s % 2 != 0:
            return False
        half = (len_s/2) - 1
        end = len_s - 1
        index = 0
        try:
            # if no error is raised the opening character is a closing bracket
            closing.index(s[index])
            return False
        except:
            # IndexError -> not a closing bracket
            print("First character was NOT a closing bracket.")
            mirror = ""
            sub_string = ""
            res = ""
            for character in s:
                print(f"char: {character}")
                if character == "(": mirror += ")"
                elif character == "[": mirror += "]"
                elif character == "{": mirror += "}"
                for bracket in closing:
                    if character == bracket:
                        print(f"Closing bracket detected.\ns.index(character) = {s.index(character)}")
                        sub_string = s[s.index(character):len(mirror)+s.index(character)]
                        print(f"sub_string ==> {sub_string}\nmirror ==> {mirror}")
                        if mirror == sub_string:
                            return True
                        else: return False









sol = Solution()

s1 = "()[]{}"
s2 = "{[]}"
s3 = "([)]"
s4 = "({[)"

print(sol.isValid(s4))
