numbers = int(input())
listu = []
count = 1
for _ in range(numbers):
    name = input()
    
    if name in listu:
        listu.append(name+str(count))
        print(name+str(count))
    else:
        listu.append(name)
        print('OK')

    
    
    
    