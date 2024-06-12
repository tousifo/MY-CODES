def hisu(n, k, listu):
    max_percipitation = 5 - k
    percipitants = 0
    
    for i in listu:
        if i <= max_percipitation:
            percipitants +=1
            
    percipitants = percipitants // 3
    
    return percipitants 
    






n, k = map(int, input().split())
listu = list(map(int, input().split()))

print(hisu(n, k, listu))