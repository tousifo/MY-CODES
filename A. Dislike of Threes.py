def lalu(n):
    coun = 0
    num = 0
    while coun < n:
        num +=1
        if num % 3 !=0 and num % 10 !=3:
            coun+=1
    return num



t = int(input())

for i in range (t):
   n = int(input())
   print(lalu(n))
   


