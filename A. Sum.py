t = int(input())

for _ in range(t):
    listu = list(map(int, input().split()))
    listu = sorted(listu)
    
    if listu[0] + listu [1] == listu [2]:
        print("YES")
    else:
        print("NO")