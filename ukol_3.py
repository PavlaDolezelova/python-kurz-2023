#nacteni json dat do slovniku
import json

with open('body.json', encoding='utf-8') as soubor:
    data = json.load(soubor)

#print(data)

#prazdny slovnik
prospech = {}

for jmeno in data.keys():
    if data[jmeno] >= 60:
        prospech[jmeno] = 'Pass'
    else:
        prospech[jmeno] = 'Fail'

#print(prospech)

#ulozeni dat ze slovniku do souboru .json
with open("prospech.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(prospech, vystupni_soubor, ensure_ascii=False, indent=4)

