
def detectCapitalUse(word: str) -> bool:
    flag = True
    upperflag = False
    first_letter = word[0]
    last_letter = word[len(word)-1]
    if first_letter.isupper() and last_letter.isupper() or first_letter.islower() and last_letter.islower():
        upperflag = True
    for letter in word:
        print(letter)
    return flag
