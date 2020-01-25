import json
from glob import glob

data = []
for file_name in glob('*.json'):
    with open(file_name) as f:
        data.append(json.load(f))

myList = []
for mob in data:
    for x in mob:
        myList.append(x['name'].lower())

myList = list(dict.fromkeys(myList))
myList.sort()


with open('mobiles.txt', 'w') as f:
    for item in myList:
        f.write("%s\n" % item)
