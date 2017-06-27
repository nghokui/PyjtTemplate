import sys, json, unittest
from code.logger import Logger 

def loadSettings():
    with open('settings.json', 'r') as jfile:
        loaded_data = json.load(jfile)
    return loaded_data

if __name__ == '__main__':
    settings = loadSettings()
    # Logger(settings).logAction('')
    