
import csv

varf = open("variations-merged2.txt")
csvf = open("paramawps-id-corrected.csv")
csvn = open("paramawps-new.csv", "w")
idfile = open("impids.txt")

# preload list of ids
ids = set()
for line in idfile:
    ids.add(int(line))

# preload variations
vardict = {}
cl = varf.readline()
cr = 0
while cl:
    if '---' in cl:
        cl = varf.readline()
        cr = int(cl)
        vardict[cr] = []
    else:
        vardict[cr].append(cl[3:].strip())
    cl = varf.readline()
# csv files

data1 = csv.reader(csvf)
data2 = csv.writer(csvn)

header = next(data1)
data2.writerow(header)

for row in data1:
    row_id = int(row[0])
    data2.writerow(row)
    if row_id in ids:
        for s in vardict[row_id]:
            row[0] = f'1000{row_id}'
            row[1] = s
            row[2] = ''
            row[5] = ''
            # row[6] = ''
            row[7] = ''
            data2.writerow(row)

