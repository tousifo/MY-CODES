n, k, l, c, d, p, nl, np = map(int, input().split())

listu = [(k*l)//nl, d*c, p//np]

aw = min(listu)

aw = aw//n

print(aw)