
# unique templates and num of operators

import json
from pprint import pprint

fname = 'file1.json'

f = open(fname, 'r')
data = json.loads(f.read())

# print(data)

unique_templates = set()
k_operators = {}
total_problems = 0
total_ops = 0


for row in data:
    total_problems += 1
    pe = ''.join(filter(lambda x: x in '+-/*()', row['Equation']))
    pel = len(''.join(filter(lambda x: x in '+-/*', pe)))
    total_ops += pel
    unique_templates.add(pe)
    if pel in k_operators:
        k_operators[pel] += 1
    else:
        k_operators[pel] = 1
    if pel == 0:
        print(row)

# pprint(unique_templates)

print(f"Number of unique templates: {len(unique_templates)}")
print("Number of problems with k operators:")
for k in sorted(k_operators):
    print(f"\tk = {k} : {k_operators[k]}")
print(f"Average number of operators: {total_ops / total_problems}")
print(f"Number of problems: {total_problems}")

