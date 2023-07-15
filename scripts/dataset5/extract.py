#%%
import re

f = open('test.txt', 'r')

r = re.compile(r'^---\s(\d+)\s(\d+)\n*\s*Answer:\s*\$?(\d+(.\d)*)\s*', re.MULTILINE)

s = f.read()

mts = r.finditer(s)

gpt_3_5_res = {}

for m in mts:
    _, id, ans, _ = m.groups()
    gpt_3_5_res.update({ id: ans })

# %%

import csv
import math

f2 = open('paramawps.csv', 'r')

data = csv.reader(f2)
next(data)

ctr = 0
gctr = 0

for row in data:
    id = row[0]
    ans = float(row[4])

    # exclude non seed problems
    if int(id) > 10000:
        continue

    try:
        gptans = float(gpt_3_5_res[id])
    except KeyError:
        continue
    except ValueError:
        continue
    if math.isclose(ans, gptans):
        ctr += 1
    gctr += 1

print(gctr, ctr)
print(ctr/gctr*100)
# %%
