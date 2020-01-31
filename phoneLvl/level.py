import json
import re
import collections

with open('mobiles.txt') as f:
    mobiles = f.readlines()

with open('mobilesLvl.txt') as f:
    mobilesLvl = f.readlines()

stop = ['dual', 'sim', 'mobile', 'td-lte', '/', 'lte',]

mobiles = [x.strip() for x in mobiles] 
mobilesLvl = [x.strip() for x in mobilesLvl] 

data = dict()

for m in mobiles:
    data[m] = dict()

for x in range(10):
    try:
        for mobile in mobiles:
            for mobileLvl in mobilesLvl:
                if mobileLvl.startswith(str(mobile)):
                    key = str(mobile)
                    if key not in data:
                        data[key] = []
                    
                    splited = mobileLvl.split()[1:]

                    for s in splited:
                        skey = str(s.replace('(', '').replace(')', ''))
                        if skey not in stop:
                            if skey not in data[key]:
                                data[key][skey] = []
                                data[key][skey] = 1
                            else:
                                data[key][skey] += 1

                    # data[key].append(' '.join(mobileLvl.split()[1:]))
                    mobilesLvl.remove(mobileLvl)    

    except Exception as e:
        print(e)


for m in mobiles:
    data[m] = {k: v for k, v in sorted(data[m].items(), reverse=True, key=lambda item: item[1])}


for m in mobiles:
    mySet = set()
    try:
        for key in data[m]:
            for k in data[m]:
                try:
                    x = [i for i in range(len(key)) if key[i] != k[i]]
                    if(x[0] > 1):
                        mySet.add(k)
                        mySet.add(key)
                        
                except Exception as e:
                    pass   

        setStopKeys = set()
        if len(mySet) > 0:
            for s in mySet:
                for key in list(data[m]):
                    rng = key if len(s) > len(key) else s
                    x = [i for i in range(len(rng)) if s[i] != key[i]]
                    if len(x) > 0:
                        if s[:x[0]] not in data[m]:
                            data[m][s[:x[0]]] = []
                            data[m][s[:x[0]]] = data[m][key] 
                        else:
                            data[m][s[:x[0]]] += data[m][key]
                    
                    setStopKeys.add(key)
        
    except Exception as e:
        print(e)

json = json.dumps(data)
f = open("dict.json","w")
f.write(json)
f.close()


