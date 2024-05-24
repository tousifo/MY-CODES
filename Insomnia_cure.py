def damaged_dragons(k, l, m, n, d):
    damgd_d = 0
    
    for i in range (1, d+1):
        if (i%k == 0 or  i%l == 0 or i%m == 0 or i%n == 0 ):
            damgd_d +=1
    return damgd_d

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

print(damaged_dragons(k, l, m, n, d))