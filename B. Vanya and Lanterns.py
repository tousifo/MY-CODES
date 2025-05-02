import sys

n, l = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

a.sort()

if n > 1:
    maxgap = max(a[i] - a[i-1] for i in range(1, n))
else:
    maxgap = 0

left_end  = a[0]
right_end = l - a[-1]
d = max(left_end, right_end, maxgap / 2)

print("{:.10f}".format(d))
