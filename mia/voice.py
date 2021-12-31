import os
import random
import subprocess


def answer(yes):
    if yes:
        exec_tts(f"Yes, sir")
    else:
        exec_tts(f"No, sir")



def good_morning(name):
    morning_phrases = {0: "Did you sleep well?", 1: "How was your night?", 
            2: "Have you been sleeping good tonight?"}

    n = random.randint(0, len(morning_phrases)-1)
    print(n)
    exec_tts(f"Good morning, {name}.")
    exec_tts(morning_phrases.get(n))
    

def good_night(name):
    night_phrases = {0: "Sleep tight.", 1: "See you tomorrow.", 
            2: "I'll get some rest too."}

    n = random.randint(0, len(night_phrases)-1)
    print(n)
    exec_tts(f"Good night, {name}.")
    exec_tts(night_phrases.get(n))
    


def exec_tts(string):
    os.system('echo %s | festival --tts' %string)
    
