n = int(input())

for _  in range(n):
    str1, str2 = input().split()
    new_str1 = str2[0] + str1[1:]
    new_str2 = str1[0] + str2[1:]
    
    print(new_str1, new_str2)
        