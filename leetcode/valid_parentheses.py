#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        len_s = len(s)
        half = (len_s/2) - 1
        if half % 2 != 0:
            return False
        end = len_s - 1
        index = 0
        while index < end:
            if s[index] == s[index+1]:
                index += 2
            else:
                if s[index] != s[end-index]:
                    return False
                index += 1
        return True
