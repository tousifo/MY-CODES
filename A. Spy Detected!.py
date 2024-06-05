t = int(input())

for _ in range(t):
    n = int(input())
    listu = list(map(int, input().split()))
    majority = 0
    
    if listu[0] == listu[1]:
        majority = listu[0]
    elif listu[0] == listu[2]:
        majority = listu[0]
    else:
        majority = listu[1]
        
    for i in range(n):
        if majority != listu[i]:
            print (i+1)
        
    