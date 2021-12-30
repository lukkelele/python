import speech_recognition as sr
from operation import main

# Find device index

ear = sr.Recognizer()
with sr.Microphone(device_index=3) as mic:
    print("Say something: ")
    audio = ear.listen(mic, timeout=3)
    print("Audio recorded.")

try:
    text = ear.recognize_google(audio)
    print(f"Text: {text}")
    main(op_text=text)
except:
    print(f"Audio could not be recognized")

