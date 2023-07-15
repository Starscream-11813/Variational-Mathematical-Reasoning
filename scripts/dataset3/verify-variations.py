
f1 = open('impids.txt')
f2 = open('variations-merged2.txt')

l = f2.readlines()

for line in f1:
    s1 = f'--- {line}'
    if s1 not in l:
        print(line)
