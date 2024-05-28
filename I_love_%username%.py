n = int(input())

listu = list(map(int, input().split()))

count = 0
bestP = listu[0]
worstp = listu[0]

for i in range(1, n):
    if listu[i] > bestP:
        bestP = listu[i]
        count +=1
    else:
        if listu[i] < worstp:
            worstp = listu[i]
            count +=1
    
print(count)
