
import csv
import re

fname = 'mawpscopy-2.csv'

ptn = r'(\d{1,3}(,\d{3})+)|(\d+)(\.\d+)?'

f = open(fname, 'r')
data = csv.reader(f)
next(data)

total_consts = 0
total_q_text = 0
total_q_eqn = 0
total_problems = 0

for row in data:
    idx, text, _, eqn, ans, _, _, have_const = row
    total_consts += 1 if have_const == 'true' else 0
    total_q_text += len(re.findall(ptn, text))
    total_q_eqn += len(re.findall(ptn, eqn))
    total_problems += 1

print(f"average number of quantities per problem: {total_q_text / total_problems}")
print(f"average number of quantities per equation: {total_q_eqn / total_problems}")
print(f"problems with constants: {total_consts}")