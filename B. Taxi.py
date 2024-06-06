def ned_taxi(n, group):
    from collections import Counter
    count = Counter(group)
    taxis = 0
    taxis += count[4]
    
    combi_3_1 = min(count[3], count[1])
    taxis += combi_3_1
    count[3] -=combi_3_1
    count[1] -= combi_3_1
    
    taxis += count[3]
    taxis += count[2]//2
    rem_2 = count[2]%2
    
    if rem_2:
        if count[1] > 2:
            taxis +=1
            count[1] -=2
        else:
            taxis +=1
            count[1] = 0
    if count[1] > 0:
        taxis += (count[1] + 3)//4
        
    return taxis
    
n = int(input())
group = list(map(int, input().split()))

print(ned_taxi(n, group))
            
    