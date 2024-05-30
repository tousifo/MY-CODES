def check_pass(n, passu):
    numbu = []
    lettu = []
    letter_encountered = False
    
    for i in passu:
        if i.isdigit():
            if letter_encountered:
                return "NO"
            numbu.append(i)
        else:
            letter_encountered = True
            lettu.append(i)
    
    if numbu != sorted(numbu):
        return "NO"
    if lettu != sorted(lettu):
        return "NO"
    return "YES"
        



t = int(input())

for _ in range(t):
    n = int(input())
    passu = input()
    print(check_pass(n, passu))
    
    
