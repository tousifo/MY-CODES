n, k = map(int, input().split())

count = 1

while True:
    total_cost = count * n
    if total_cost % 10 == 0 or total_cost % 10 == k:
        print (count)
        break
    count += 1
    
    