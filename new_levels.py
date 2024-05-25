def can_pass_all_levels(n, x_levels, y_levels):
    # Create a set of levels that either X or Y can pass
    levels_covered = set(x_levels) | set(y_levels)
    
    # Check if the set contains all levels from 1 to n
    return set(range(1, n+1)) == levels_covered

# Read input
n = int(input())
p = int(input().split()[0])
x_levels = list(map(int, input().split()[1:]))
q = int(input().split()[0])
y_levels = list(map(int, input().split()[1:]))

# Check if they can pass all levels
if can_pass_all_levels(n, x_levels, y_levels):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")