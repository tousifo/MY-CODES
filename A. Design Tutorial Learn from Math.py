n = int(input())

if n == 12:
    print("4", "8")
elif n == 13:
    print('8', '5')
elif n==14:
    print('8', '6')
else:
    n = n - 12
    print('12', n)