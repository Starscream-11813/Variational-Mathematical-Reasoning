
import json

# check which mawps failures passed in paramawps

d1 = 'DeBERTaGen-mawps-single'
d2 = 'DeBERTaGen-paramawps'

data1 = []
data2 = []
failureids = []

succ = {}
cum = {}

for foldnum in range(0, 5):
    fname1 = f'{d1}/fold{foldnum}/generation_result.json'
    fname2 = f'{d2}/fold{foldnum}/generation_result.json'
    f1 = open(fname1)
    f2 = open(fname2)
    a1 = json.load(f1)
    a2 = json.load(f2)
    data1.extend(a1)
    data2.extend(a2)

for row in data1:
    baseid = row['id']
    if row['value acc'] == False:
        failureids.append(baseid)
        cum[baseid] = 0
        succ[baseid] = 0
        # print(row)

for row in data2:
    baseid = row['id'] % 10000
    if baseid in failureids:
        cum[baseid] += 1
        if row['value acc'] == True:
            succ[baseid] += 1

count = 0
count2 = 0

for i in failureids:
    if cum[i] == 0:
        continue
    count2 += 1
    pcnt = succ[i] / cum[i]
    if pcnt > 0.5:
        count += 1
        print(i)

print('\n')

print(f'total problems: {count2}')
print(f'total solved: {count}')
print(f'percentage: {count / count2 * 100}')
