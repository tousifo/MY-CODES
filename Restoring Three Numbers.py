listu = list(map(int, input().split()))

listu.sort()

sum = listu[3]

a = sum - listu[0]
b = sum - listu[1]
c = sum - listu [2]

print(a, b, c)