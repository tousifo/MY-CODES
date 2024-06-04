n = int(input())
listu = list(map(int, input().split()))

serja = 0
dima = 0

left = 0
right = n-1

for i in range (n):
    if i%2 == 0:
        if listu[left] >= listu[right]:
            serja +=listu[left]
            left +=1
        else:
            serja += listu[right]
            right-=1
    else:
        if listu[left] >= listu[right]:
            dima +=listu[left]
            left +=1
        else:
            dima += listu[right]
            right -=1
            
print(serja, dima)