import speech_recognition as sr
from operation import main

# index device=1 for proper mic

ear = sr.Recognizer()
with sr.Microphone(device_index=1) as mic:
    print("Say something: ")
    audio = ear.listen(mic, timeout=3)
    print("Audio recorded.")

try:
    text = ear.recognize_google(audio)
    print(f"i heard: {text}")
    main(op_text=text)
except:
    print(f"Audio could not be recognized")

