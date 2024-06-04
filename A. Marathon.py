n = int(input())

for _ in range(n):
    listu =list (map(int, input().split()))
    count = 0
    for i in range(1, 4):
        if listu[0] < listu[i]:
            count +=1
    print(count)    
        