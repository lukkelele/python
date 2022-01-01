from operation import think
import speech_recognition as sr
import os
import voice
import pyttsx3


# index device=1 for proper mic
host = "Lukas"


def init_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)
    engine.setProperty('rate', 200)
    return engine


# Is not used yet but will be the main method for running Mia
def run():
    engine = init_engine()
    ear = sr.Recognizer()
    mute = 0
    on = True
    with sr.Microphone(device_index=1) as mic:
        while on:  
            while mute == 0:
                audio = ear.listen(mic, timeout=4)
                try:
                    text = ear.recognize_google(audio)
                    engine.say(text)
                    think(operation=text)
                except:
                    print("Audio could not be recognized")
         

def say(string):
    engine.say(string)
    engine.runAndWait()


voice.good_morning(host)
voice.good_night(host)

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





