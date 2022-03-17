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
        flag = False
        if s[index] == s[index+1]:
            flag = True
        while index < half and flag == False:
            if s[index] != s[end-index]:
                return False
            index += 1
        if flag == False: return True
        else:
            index = 0
            if len_s == 2:
                return True
            while index < end:
                if s[index] != s[index+1]:
                    return False
                index += 2
            return True
