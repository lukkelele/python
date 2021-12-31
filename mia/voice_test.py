import pyttsx3
import os
from subprocess import call

engine = pyttsx3.init()
voices = engine.getProperty('voices')
i = 0

s = "Im a program made by Lukas Gunnarsson to help him with tasks in his daily life. My name is Mia."
os.system('echo %s | festival --tts' %s)

# Voice in festvox /usr/share/festival/voices
# women voice (voice_cmu_us_slt_cg)
