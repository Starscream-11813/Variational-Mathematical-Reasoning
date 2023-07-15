
import csv
import re
from pprint import pprint

# fname = 'file2-3.csv'
fname = 'mawpscopy.csv'

gi = 0
nums = []
con = False

cur_row_id = None
dup_ids = set()

f = open(fname, 'r')
data = csv.reader(f)
next(data)

new_data = []

ptn = r'(\d{1,3}(,\d{3})+)|(\d+)(\.\d+)?'

def parse_num(s: str) -> int | float:
    """
    returns and int or a float from number string
    """
    num = float(s.replace(',', ''))
    if num.is_integer():
        return int(num)
    return num

def replace_num(mt : re.Match) -> str:
    """
    called for every instance of a number found in problem text
    """
    global gi, nums, cur_row_id, dup_ids
    gi += 1
    q = f'[Q{gi}]'
    n = parse_num(mt.group(0))
    for tup in nums:
        if tup[0] == n:
            # print(f'warning: duplicate {n} in {cur_row_id}')
            dup_ids.add(cur_row_id)
    nums.append((n, q))
    return q

def replace_num_eqn(mt : re.Match) -> str:
    """
    called for every instance of a number found in equation
    """
    global nums, con
    s = mt.group(0)
    num = parse_num(s)
    for tup in nums:
        if tup[0] == num:
            return tup[1]
    con = True
    return s



for row in data:
    row_id, text, _, eqn, _ = row
    # print(text)
    nums = []
    gi = 0
    con = False
    cur_row_id = row_id
    # print(text)
    ntext = re.sub(ptn, replace_num, text)
    # print(ntext)
    # print(nums)
    # print(eqn)
    neqn = re.sub(ptn, replace_num_eqn, eqn)
    # print(neqn)
    # print(f'have_constant: {con}')
    row.append(ntext)
    row.append(neqn)
    row.append(str(con).lower())
    new_data.append(row)

of = open('rs.csv', 'w')
op = csv.writer(of)

op.writerows(new_data)

pprint(dup_ids)
