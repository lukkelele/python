# Used for reading output logs of gameplay
from datetime import datetime


def open_log(path):
    log = open(f"{path}", 'r')
    return log

def read_log(file):
    for line in file:
        print(f"CURRENT LINE: {line}", end="")

# Debugging 
def open_file_msg(path):
    print(f"[{datetime.now()}]  Opening file at {path}")

