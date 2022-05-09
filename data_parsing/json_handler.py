import json

def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Input --> dict
def convert_to_json(file):
    return json.dumps(file)

# Input --> json
def convert_to_dict(file):
    conv_json = json.loads(file)
    return conv_json

def write_json(data, output='data.json'):
    with open(output, 'w') as json_file:
        json.dump(data, json_file, indent=2)
