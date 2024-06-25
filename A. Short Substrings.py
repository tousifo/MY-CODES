n = int(input())

for _ in range(n):
    stir = input()
    paw = []
    if len(stir) <= 2:
        paw = list(stir)
    else:
        paw.append(stir[0])
        for i in range (1, len(stir)-1, 2):
            paw.append(stir[i])
        paw.append(stir[-1])
    print(''.join(paw))