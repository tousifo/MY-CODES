
namu_1 = input()
namu_2 = input()
ulu = input()

puka = namu_1 + namu_2

puka = sorted(puka)
ulu = sorted(ulu)

if puka == ulu:
    print('YES')
else:
    print('NO')