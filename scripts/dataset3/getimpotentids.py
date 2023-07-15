
import csv
from time import sleep

fname = 'paramawps-id-corrected.csv'

f = open(fname, 'r')
data = csv.reader(f)
header = next(data)

impotent_ids = set()
non_impotent_ids = set()

for row in data:
    # print(int(row[0]))
    row_id = int(row[0])
    if (row_id > 10000):
        # print(row_id)
        non_impotent_ids.add(row_id % 10000)

# print(sorted(non_impotent_ids))

f.seek(0)
header = next(data)
n = open("impids.txt", "w")

for row in data:
    row_id = int(row[0])
    if (row_id not in non_impotent_ids and row_id < 10000 and row_id > 522):
        print(row_id)
        # n.write(f"--- {row_id}\n")
        # impotent_ids.add(row_id)
        n.write(str(row_id) + '\n')
        # v = gv(row[1])
        # n.write(v)
        # n.write('\n')
        n.flush()

# print(sorted(impotent_ids))

# print(len(impotent_ids))
