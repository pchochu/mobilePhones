import json
import re

with open('mobiles.txt') as f:
    mobiles = f.readlines()

with open('mobilesLvl.txt') as f:
    mobilesLvl = f.readlines()

mobiles = [x.strip() for x in mobiles] 
mobilesLvl = [x.strip() for x in mobilesLvl] 


data = dict()
try:
    for mobile in mobiles:
        for mobileLvl in mobilesLvl:
            print(mobile + '----------->' + mobileLvl.split()[0])
            if(mobile in mobileLvl.split()[0]):
                key = str(mobile)
                if key not in data:
                    data[key] = []

                data[key].append(mobileLvl)
                mobilesLvl.remove(str(mobileLvl))

except Exception as e:
    print(e)




