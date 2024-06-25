t = int(input())

for _ in range(t):
    listu = list(map(int, input().split()))
    
    listu = sorted(listu)
    
    print(listu[1])