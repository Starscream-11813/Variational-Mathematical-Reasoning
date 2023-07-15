
import json
from sympy import *

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

print(len(set(failureids)))

families = {}

for row in data2:
    # print(e['id'])
    if ('NUM' in row['prediction'] or 'NUM' in row['target'] or 'UNK' in row['prediction'] or 'UNK' in row['target'] or '=' not in row['prediction'] or '=' not in row['target']):
        continue
    if (str(row['id'])[:5] == '16000'):
        continue
    base_id = row['id'] % 10000
    if base_id not in failureids:
        continue
    if base_id not in families.keys():
        families[base_id] = []
    families[base_id].append(row)

total = 0
correct = 0
for family in families:
    freq_pred = {}
    freq_targ = {}
    for member in families[family]:
        try:
            x = symbols('x')
            pred_s = member['prediction'].split('=')
            targ_s = member['target'].split('=')
            pred = Eq(sympify(pred_s[0]), sympify(pred_s[1]))
            targ = Eq(sympify(targ_s[0]), sympify(targ_s[1]))
            result = solve(pred, x)[0]
            result_targ = solve(targ, x)[0]
            if result not in freq_pred.keys():
                freq_pred[result] = 0
            freq_pred[result] += 1
            if result_targ not in freq_targ.keys():
                freq_targ[result_targ] = 0
            freq_targ[result_targ] += 1
        except:
            pass

    # print(freq_pred, family)
    # print(freq_targ, family)

    try:
        pred_val = max(freq_pred, key=freq_pred.get)
        targ_val = max(freq_targ, key=freq_targ.get)

        if(pred_val == targ_val):
            correct += 1

        total += 1
    except:
        pass


# for row in data2:
#     baseid = row['id'] % 10000
#     if baseid in failureids:
#         cum[baseid] += 1
#         if row['value acc'] == True:
#             succ[baseid] += 1

print(f'Total unsolved problems in MAWPS: {len(failureids)}')
print(f'reoccuring unsolved problems in ParaMAWPS: {len(families)}')
print(f'Solved reoccuring problems: {correct}')
print(f'Percentage: {correct / total * 100}')
