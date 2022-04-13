import json

import os

from dicio import Dicio

from datetime import datetime

dicio = Dicio()

def processString(txt):
    specialChars = '"[](\')'
    for specialChar in specialChars:
        txt = txt.replace(specialChar,'')
    txt = txt.replace('Word', '')
    return txt

print('Por favor digite a palavra principal:')

word = input()

result = dicio.search(word)

data = str(result.synonyms)

cleanString = processString(data)

strToJson = json.dumps(cleanString, ensure_ascii=False)

ts = datetime.timestamp(datetime.now())

ts = str(ts)

fileName = ts + '_result.txt'

with open(os.getcwd() + '/' + fileName, 'w', encoding='utf-8') as f:
    json.dump(strToJson.replace('"',''), f, ensure_ascii=False, indent=4)
