n = int (input())
listu = list(map(int, input().split()))
count = 0
maxi = 0

for i in range(n-1):
    if listu[i+1] >= listu[i]:
        count +=1
    else:
        maxi = max(maxi, count)
        count = 0
        

maxi = max(maxi, count)

print(maxi+1)
