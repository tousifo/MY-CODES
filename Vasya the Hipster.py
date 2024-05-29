a, b = map(int, input().split())

dif_day = min(a, b)

a -= dif_day
b -= dif_day

sam_day = (a+b) // 2

print(dif_day, sam_day)