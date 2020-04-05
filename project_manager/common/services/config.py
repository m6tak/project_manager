import json

def load():
    with open('config.json') as config_file:
        return json.load(config_file)

