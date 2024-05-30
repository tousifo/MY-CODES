t = int(input())

for _ in range (t):
    n = int (input())
    listu = list(map(int, input().split()))
    listu = sorted(listu)
    result = "YES"
    for i in range(1, n):
        if listu[i] - listu[i-1] >= 2:
            result = "NO"
            break
    print(result)