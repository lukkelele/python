from operation import main
import speech_recognition as sr
import os

# index device=1 for proper mic

ear = sr.Recognizer()
with sr.Microphone(device_index=1) as mic:
    print("Say something: ")
    audio = ear.listen(mic, timeout=3)
    print("Audio recorded.")

try:
    text = ear.recognize_google(audio)
    main(op_text=text)
except:
    print(f"Audio could not be recognized")

