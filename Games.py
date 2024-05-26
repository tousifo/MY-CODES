def chek_match(uniforms):
    home_uni = {}
    guest_uni = {}
    
    for h, g in uniforms:
        if h in home_uni:
            home_uni[h] += 1
        else:
            home_uni[h] = 1
        if g in guest_uni:
            guest_uni[g] += 1
        else:
            guest_uni[g] = 1
        counta = 0
            
    for homcol in home_uni:
        if homcol in guest_uni:
            counta += home_uni[homcol] * guest_uni[homcol]
            
    return counta
            



n = int(input())

uniforms = [tuple(map(int, input().split())) for _ in range(n)]

print(chek_match(uniforms))

