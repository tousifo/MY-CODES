n = int(input())
listu = []
name_count = {}

for _ in range(n):
    name = input()
    
    if name in name_count:
        count = name_count[name]
        new_name = f"{name}{count}"
        name_count[name] += 1
    
        while new_name in name_count:
            count += 1
            new_name = f"{name}{count}"
        
        name_count[new_name] = 1
        listu.append(new_name)
        print(new_name)
    else:
        name_count[name] = 1
        listu.append(name)
        print("OK")
