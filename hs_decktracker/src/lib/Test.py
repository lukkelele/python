import json

with open("./decks.json") as f:
    s = json.load(f)
    k = 0
    while k < 2:
        print(s[k])
        k+=1
