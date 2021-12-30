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





