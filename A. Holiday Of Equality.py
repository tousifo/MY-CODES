def is_composite(n, sieve):
    return not sieve[n] and n > 1

def generate_sieve(limit):
    sieve = [False] * (limit + 1)
    sieve[0] = sieve[1] = True
    for start in range(2, int(limit**0.5) + 1):
        if not sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = True
    return sieve

def find_composite_pair(n):
    sieve = generate_sieve(n)
    for x in range(4, n):
        if is_composite(x, sieve) and is_composite(n - x, sieve):
            return x, n - x


n = int(input().strip())

x, y = find_composite_pair(n)
print(x, y)
