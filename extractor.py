import nltk
import json
import re
from nltk.tokenize import word_tokenize

with open('entities.json') as file:
    data = json.load(file)

def compiler(entity):
    wrds = '|'.join(word_tokenize(' '.join(list(data.values())[entity])))
    return re.compile(wrds)

def chat():
    entities = []
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        for i in range(4):
            if compiler(i).search(inp):
                entities.append(list(data.keys())[i])

        print("entities: " + str(entities))
        entities.clear()


chat()