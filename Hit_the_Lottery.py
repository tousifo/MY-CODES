def min_bills(n):
    listu = [100, 20, 10, 5, 1]
    count = 0
    
    for i in listu:
       count+= n//i
       n = n%i
       
        
    
    return count

n = int(input())

print(min_bills(n))