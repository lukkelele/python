import webbrowser
from urllib.parse import urlencode

voice_commands = ['open', 'visit', 'check', 'look up', 'mute', 'execute', 'show me']
long_voiceCommands = ['show me', 'look up', 'turn on']


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



def predict_website(command):
    print("visiting website --> ", end=' ')
    org_cmd = command
    command = command.lower().replace(' ','')
    web_dict = {'youtube': 'youtube.com', 'facebook': 'facebook.com', 'codespeedy': 'codespeedy.com',
                'quora': 'quora.com', 'amazon': 'amazon.in'} 
    if command in web_dict.keys():
        website = f"https://www.{web_dict[command]}/"
        print("Website to open --> " + website)
        webbrowser.open_new(website)
    else:
        q = {'q': org_cmd}
        query = urlencode(q)
        complete_url = f"https://www.google.com/search?{query}"
        print("Complete url --> "+complete_url)
        webbrowser.open_new(complete_url)


    


def think(operation):
    print(f"OPERATION: {operation}")
    operation = operation.lower()
    s = scan_command(operation)
    if s != '':
        predict_website(s)
    else:
        print(f"\nCouldn't process information correctly")

