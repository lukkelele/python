import os
import random
import subprocess


def answer(yes):
    if yes:
        exec_tts(f"Yes, sir")
    else:
        exec_tts(f"No, sir")



def good_morning(name):
    n = random.randint(0,2)
    print(n)
    morning_phrases = {0: "Did you sleep well?", 1: "How was your night?", 
            2: "Have you been sleeping good tonight?"}

    exec_tts(f"Good morning, {name}.")
    exec_tts(morning_phrases.get(n))
    


def exec_tts(string):
    os.system('echo %s | festival --tts' %string)
    
