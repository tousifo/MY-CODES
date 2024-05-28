listu = list(map(int, input().split()))

listu.sort()

distu = (listu[1]-listu[0])+(listu[2]-listu[1])

print(distu)