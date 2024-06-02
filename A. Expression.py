a = int(input())
b= int(input())
c = int(input())

resu = [
    a + b + c,
    a + b * c,
    a * b + c,
    a * b * c,
    (a + b) * c,
    a * (b + c)
]

max_v = max(resu)

print(max_v)