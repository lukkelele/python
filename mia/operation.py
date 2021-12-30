import webbrowser
from urllib.parse import urlencode


def main(op_text):
    print(f"OPERATION: {op_text}")
    op_text = op_text.lower()
    if op_text.startswith('visit') or op_text.startswith('show me') or op_text.startswith('open'):
        if ' ' in op_text:
            command = refine(op_text)
            prediction = predict_website(command)
        else:
            print(f"\nCouldn't process information correctly")

if __name__ == '__main__':
    text = 'visit '
    main(text)



def refine(string):
    words = string.split(" ")
    if len(words) == 0:
        return ''   # If empty
    else:
        if string.startwith('show me'):
            return ' '.join(words[2:]).strip(' ')
        else:
            return ' '.join(words[1:]).strip(' ')


def predict_website(command):
    print(f"visiting website --> ", end=' ')
    org_cmd = command
    command = command.lower().replace(' ','')
    web_dict = {'youtube': 'youtube.com'}
    if command in web_dict.keys():
        website = f"https://www.{web_dict[command]}/"
        print(website)
        webbrowser.open_new(website)
    else:
        q = {'q': org_cmd}
        query = urlencode(q)
        complete_url = f"https://www.google.com/search?{query}"
        print(complete_url)
        webbrowser.open_new(complete_url)

