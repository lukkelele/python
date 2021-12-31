import webbrowser
import os
import subprocess
from urllib.parse import urlencode


voice_commands = ['open', 'visit', 'check', 'look up', 'mute', 'execute', 'show me']
long_voiceCommands = ['show me', 'look up', 'turn on']
web_dict = {'youtube': 'youtube.com', 'facebook': 'facebook.com', 'codespeedy': 'codespeedy.com',
            'quora': 'quora.com', 'amazon': 'amazon.in'} 
exec_dict = {'spotify': '/usr/bin/spotify', 'alacritty': '/usr/bin/alacritty'}

#
#   Read calendar, read weather, check notifications
#   Check time, mute, start music, adjust volume, 
#   Control blinds, reminders
#


def scan_command(string):
    for command in voice_commands:
        if string.startswith(command):
            if ' ' in string:
                return refine(string)
        else:
            return ''



def refine(string):
    words = string.split(' ')
    if len(words) == 0:
        return ''
    else:
        for cmd in long_voiceCommands:
            if string.startswith(cmd):
                return ' '.join(words[2:]).strip(' ')
            else:
                return ' '.join(words[1:]).strip(' ')  # for open and visit command


def predict(command):
    command = command.lower().replace(' ','')
    if command in web_dict.keys():
        predict_website(command)
    
    elif command in exec_dict.keys():
        predict_application(command)
    
    # Search if no other option get selected
    else:
        q = {'q': command}
        query = urlencode(q)
        complete_url = f"https://www.google.com/search?{query}"
        print("Complete url --> "+complete_url)
        webbrowser.open_new(complete_url)



def predict_application(command):
    if command in exec_dict.keys():
        print(f"launching {command}")
        subprocess.call(['/usr/bin/{command}']) 
    else:
        print(f"couldnt launch {command}")



def predict_website(command):
    website = f"https://www.{web_dict[command]}/"
    print("Website to open --> " + website)
    webbrowser.open_new(website)



def think(operation):
    print(f"OPERATION: {operation}")
    operation = operation.lower()
    s = scan_command(operation)
    if s != '':
        predict(s)
    else:
        print(f"\nCouldn't process information correctly")

