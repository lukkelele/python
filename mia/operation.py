import webbrowser
from urllib.parse import urlencode


def repeat(word):
    print(word)



def refine(string):
    words = string.split(' ')
    if len(words) == 0:
        return ''
    else:
        if string.startswith('show me'):
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


def main(op_text):
    print(f"OPERATION: {op_text}")
    op_text = op_text.lower()
    if op_text.startswith('visit') or op_text.startswith('show me') or op_text.startswith('open'):
        if ' ' in op_text:
            print("refining..")
            command = refine(op_text)
            print("refine done")
            predict_website(command)
        else:
            print(f"\nCouldn't process information correctly")


if __name__ == '__main__':
    text = 'visit '
    main(text)

