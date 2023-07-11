
#%%
import json
from sympy import *

f = open('generation_result.json')
data = json.load(f)

families = {}

for e in data:
    # print(e['id'])
    if ('NUM' in e['prediction'] or 'NUM' in e['target'] or 'UNK' in e['prediction'] or 'UNK' in e['target'] or '=' not in e['prediction'] or '=' not in e['target']):
        continue
    if (str(e['id'])[:5] == '16000'):
        continue
    base_id = e['id'] % 10000
    if base_id not in families.keys():
        families[base_id] = []
    families[base_id].append(e)

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

    print(freq_pred, family)
    print(freq_targ, family)

    try:
        pred_val = max(freq_pred, key=freq_pred.get)
        targ_val = max(freq_targ, key=freq_targ.get)

        if(pred_val == targ_val):
            correct += 1

        total += 1
    except:
        pass
    print('--------------------------------------------------------------------')

print(correct / total)


# %%
