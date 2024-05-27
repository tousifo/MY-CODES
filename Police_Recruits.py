n = int (input())
listu = list(map(int, input().split()))

avai_offi = 0
crimu = 0

for i in listu:
    if i == -1:
        if avai_offi > 0:
            avai_offi -= 1
        else:
            crimu += 1
    else:
        avai_offi +=i

print(crimu)
    
    