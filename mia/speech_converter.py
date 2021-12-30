from operation import main
import speech_recognition as sr
import os
import pyttsx3

# index device=1 for proper mic

ear = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)
engine.setProperty('rate', 200)
with sr.Microphone(device_index=1) as mic:
    print("Say something: ")
    audio = ear.listen(mic, timeout=3)
    print("Audio recorded.")

try:
    text = ear.recognize_google(audio)
    engine.say(text)
    engine.runAndWait()
    main(op_text=text)
except:
    print("Audio could not be recognized")

