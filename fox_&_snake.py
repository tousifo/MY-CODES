a, b = map(int, input().split())

for i in range(1, a + 1):
    if i % 2 != 0:
        # Odd rows (1, 3, 5, ...)
        for j in range(1, b + 1):
            print('#', end='')
    else:
        # Even rows (2, 4, 6, ...)
        if (i // 2) % 2 == 1:
            # End with '#'
            for j in range(1, b + 1):
                if j == b:
                    print('#', end='')
                else:
                    print('.', end='')
        else:
            # Start with '#'
            for j in range(1, b + 1):
                if j == 1:
                    print('#', end='')
                else:
                    print('.', end='')
    print()  # Move to the next line after each row
