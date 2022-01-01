## Mia
---
I got bored and tried designing a knock-off Jarvis from *Iron-Man*.  
  
Pyttsx3 is not fully functional on Linux with the voices not working properly.  
It is probably an issue with espeak but I've tried with the different espeak packages from AUR (ArchLinux User Repository).  
As a quick solution I'm calling an echo with a text which pipes to *festival* to voice the text.  
I'm not fully comfortable using os.system too much but to simulate a voice that actually sounds like a voice it is something that will have to do for now.  
  
To weave in as much learning as possible, I'm thinking about using python to execute scripts to control a microcontroller that runs on c.  
This may seem unneccessary since the compiled C code would already exist on a microcontroller, but I learn a lot this way.  
