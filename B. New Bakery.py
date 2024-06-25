def max_profit(n, a, b):
    def revenue(k):
        return k * (2*b - k + 1) // 2 + (n - k) * a

    # Consider k = 0 (all buns sold at regular price)
    max_revenue = n * a

    # Find the optimal k
    # The revenue function is quadratic in k, so the maximum will be at one of the endpoints
    # or where the derivative is zero (which occurs at k = b - a + 1)
    potential_k = [0, min(n, b), min(n, b, max(0, b - a + 1))]

    for k in potential_k:
        max_revenue = max(max_revenue, revenue(k))

    return max_revenue

# Read input
t = int(input())  # number of test cases

for _ in range(t):
    n, a, b = map(int, input().split())
    print(max_profit(n, a, b))