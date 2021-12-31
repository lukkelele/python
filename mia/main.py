from operation import think
import speech_recognition as sr
import os
import pyttsx3

# index device=1 for proper mic



def init_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)
    engine.setProperty('rate', 200)
    return engine


def run():
    engine = init_engine()
    ear = sr.Recognizer()
    mute = 0
    on = True
    with sr.Microphone(device_index=1) as mic:
        while on:  
            while mute == 0:
                audio = ear.listen(mic, timeout=4)
                print(f"I heard {audio}")
                try:
                    text = ear.recognize_google(audio)
                    engine.say(text)
                    think(operation=text)
                except:
                    print("Audio could not be recognized")
         

def say(string):
    engine.say(string)
    engine.runAndWait()



ear = sr.Recognizer()
engine = init_engine()

with sr.Microphone(device_index=1) as mic:
    print("Say something: ")
    audio = ear.listen(mic, timeout=2)
    print("Audio recorded.")

try:
    text = ear.recognize_google(audio)
    say(text)
    think(operation=text)
except:
    print("Audio could not be recognized")





