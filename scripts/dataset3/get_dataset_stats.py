
# unique templates and num of operators

from pprint import pprint
import csv
import re
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fname')
args = parser.parse_args()

fname = args.fname

f = open(fname, 'r')
data = csv.reader(f)
next(data)

unique_templates = set()
k_operators = {}
total_problems = 0
total_ops = 0

# def convert_prefix(eqn : str) -> str:
#     pass

for row in data:
    total_problems += 1
    pe = ''.join(filter(lambda x: x in '+-/*()', row[3]))
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

