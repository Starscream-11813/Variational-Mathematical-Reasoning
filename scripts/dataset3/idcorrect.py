
# id correction

import csv

fname = 'paramawps-new.csv'

f = open(fname, 'r')
data = csv.reader(f)
header = next(data)

f2 = open('paramawps-new2.csv', 'w')
n = csv.writer(f2)

n.writerow(header)

last_seed_id = None
current_sub_id = 1
new_data = []

for row in data:
    # print(int(row[0]))
    row_id = int(row[0])
    if (row_id > 10000):
        # print(row_id)
        new_row_id = str(current_sub_id * 1000) + str(last_seed_id)
        current_sub_id += 1
        # print(new_row_id, row_id)
        row[0] = new_row_id
        new_data.append(row)
    else:
        current_sub_id = 1
        last_seed_id = row_id
        new_data.append(row)

# print(new_data)
n.writerows(new_data)
