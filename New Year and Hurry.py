n, t = map(int, input().split())
a = 0
count = 0

for i in range(1, n+1):
    a += 5 * i
    if   t + a <= 240:
        count+=1
    else:
        break
        
print(count)