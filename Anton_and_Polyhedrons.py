def kaz(n, listu):
    
    dicu = {
    "Tetrahedron" : 4,
    "Cube" : 6,
    "Octahedron" : 8,
    "Dodecahedron" : 12, 
    "Icosahedron" : 20
    }
    count = 0
    for i in listu:
        if i in dicu.keys():
            count += dicu[i]
            
    return count



n = int(input())
listu = []
for _ in range(n):
    valu = input().strip()
    listu.append(valu)

print (kaz(n, listu))