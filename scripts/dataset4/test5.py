import json

f = open('DeBERTaGen-mawps-single/fold1/generation_result.json')

data = json.load(f)

count = 0
total = 0

for row in data:
    if row['value acc'] == True:
        count += 1
    total += 1

print(count, total, f'{count / total * 100}')
