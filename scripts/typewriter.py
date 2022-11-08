from sys import stdout, argv
import os, time

message = argv[1]
message_length = len(message)

print(f"Passed message: {message}")

def typewriter(msg):
    message_length = len(msg)
    for character in msg:
        if character == "\\":
            idx = msg.index(character)
            if idx != message_length and msg[idx+1] == "n":
                stdout.write("\n")
                msg = msg[idx+1:] 
                typewriter(msg)
        elif character != "\n":
            time.sleep(0.10)

        if character != "\\":
            stdout.write(character)
            stdout.flush()

    stdout.write("\n")

# os.system("cls") # windows
os.system("clear")
typewriter(message)
