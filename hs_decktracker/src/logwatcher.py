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
    print(f"{get_logmsg()}  Opening file at {path}")

def get_logmsg():
    current_time = datetime.now()
    return f"[{current_time}]" 
