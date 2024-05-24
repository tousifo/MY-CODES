def min_moves(a, b):
    return (b - (a % b)) % b

# Read input
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(min_moves(a, b))