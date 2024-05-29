def decompose_to_round_numbers(n):
    round_numbers = []
    factor = 1
    
    while n > 0:
        digit = n % 10
        if digit != 0:
            round_numbers.append(digit * factor)
        n //= 10
        factor *= 10
    
    return round_numbers

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    round_numbers = decompose_to_round_numbers(n)
    results.append((len(round_numbers), round_numbers))

for resu in results:
    k, round_numbers = resu
    print(k)
    print(" ".join(map(str, round_numbers)))
