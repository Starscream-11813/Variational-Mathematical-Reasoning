
import matplotlib
import matplotlib.pyplot as plt

mawps = {
    '1' : 1309,
    '2' : 865,
    '3' : 107,
    '4' : 41,
    '5' : 34,
    '6' : 5,
    '7' : 6,
    '8' : 2,
    '9' : 2,
    '10' : 1
}

mawpspp = {
    '1' : 2284,
    '2' : 1652,
    '3' : 428,
    '4' : 185,
    '5' : 210,
    '6' : 53,
    '7' : 70,
    '8' : 2,
    '9' : 19,
    '10' : 1
}

svamp = {
    '1' : 762,
    '2' : 237,
    '3' : 0,
    '4' : 0,
    '5' : 0,
    '6' : 0,
    '7' : 0,
    '8' : 0,
    '9' : 0,
    '10' : 0
}

matplotlib.rcParams['font.family'] = ['TeX Gyre Pagella']

# print(mawpspp, svamp)

plt.figure(figsize=(3, 3))
plt.title('MAWPS')
plt.bar(list(mawps.keys()), list(mawps.values()))
# plt.show()
plt.savefig('mawps.png')


plt.clf()

plt.figure(figsize=(3, 3))
plt.title('ParaMAWPS')
plt.bar(list(mawpspp.keys()), list(mawpspp.values()))
# plt.show()
plt.savefig('mawpspp.png')

plt.clf()

plt.figure(figsize=(3, 3))
plt.title('SVAMP')
plt.bar(list(svamp.keys()), list(svamp.values()))
# plt.show()
plt.savefig('svamp.png')
