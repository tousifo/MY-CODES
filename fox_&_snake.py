a, b = map(int, input().split())

for i in range(1, a + 1):
    if i % 2 != 0:
        for j in range(1, b + 1):
            print('#', end='')
    else:
        if (i // 2) % 2 == 1:
            for j in range(1, b + 1):
                if j == b:
                    print('#', end='')
                else:
                    print('.', end='')
        else:
            for j in range(1, b + 1):
                if j == 1:
                    print('#', end='')
                else:
                    print('.', end='')
    print()  