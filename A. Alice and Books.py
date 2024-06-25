









t = int(input())
 
for _ in range(t):
    n = int(input())
    listu = list(map(int, input().split()))
    mid = (len(listu)+1)//2
    listu1 = listu[:mid]
    listu2 = listu[mid:]
    
    laku = listu1[-1] + listu2[-1]
    print(laku)
    
