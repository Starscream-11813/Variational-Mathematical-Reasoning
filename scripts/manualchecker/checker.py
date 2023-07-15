import sys
import argparse
import csv
import os

parser = argparse.ArgumentParser()

parser.add_argument('start', help='row to start screening after')
parser.add_argument('end', help='row to end screening at')
parser.add_argument('outfile', help='file to dump faulty ids in')

args = parser.parse_args()

dump = open(args.outfile, 'a')
csvf = open('paramawps.csv', 'r')

startid = int(args.start)
endid = int(args.end)

data = csv.reader(csvf)

# store seed problems encountered
seeds = {}

# store problems to check
probs = []

# discard header
next(data)

lineno = 2

for row in data:
    rowid, probtext, _, eqn, ans, _, _, _ = row
    rowid = int(rowid)
    if (rowid < 10000):
        seeds.update({ rowid : (probtext, eqn, ans) })
    if (lineno > startid and lineno <= endid):
        probs.append((rowid, probtext, eqn, ans))
    lineno += 1

b = ''

lineno = startid

for p in probs:
    lineno += 1
    rowid, probtext, eqn, ans = p
    seed = rowid % 10000

    print('\033[2J', end='')        # linux
    # os.system('cls')                # windows

    print(b + '\n')
    print(f'Problem ID: {rowid}\tSeed: {seed}')
    print(f'Line {lineno}\n')
    print("\nSTATEMENT")
    print(probtext)
    print("\nEQUATION")
    print(eqn)
    print("\nANSWER")
    print(ans)
    print("\n---------------------------------------------------------\n")
    print("SEED PROBLEM")
    print("\nSTATEMENT")
    print(seeds[seed][0])
    print("\nEQUATION")
    print(seeds[seed][1])
    print("\nANSWER")
    print(ans)
    print("\n---------------------------------------------------------\n")

    c = input("Press ENTER if the problem is correct, otherwise input a comment to tag this problem: ")

    if (c == ''):
        b = ''
        continue
    else:
        b = f'Problem {rowid} added to dump.'
        dump.write(f'{rowid} : {c}\n')
