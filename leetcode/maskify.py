# return masked string
def maskify(cc):
   
    if len(cc) <= 4:
        return cc
    result = "";
    strlength = len(cc)
    lastDigits = strlength-5    # -4 and -1 for index as well
    substr = string[lastDigits:strlength]
    for num in lastDigits:
        result += "#"
    return result+substr



#
# return masked string
#def maskify(cc):
 #   l = len(cc)
 #   if l <= 4: return cc
 #   return (l - 4) * '#' + cc[-4:]
