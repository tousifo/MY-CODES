t = int(input())

for _ in range(t):
    a , b = map(int, input().split())
    
    if a == b:
        print("0")
    else:
        z = abs(a - b)
        count = z // 10 + (z%10 != 0)
        print(count)