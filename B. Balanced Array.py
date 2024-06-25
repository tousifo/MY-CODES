t = int(input())

for _ in range(t):
    n = int(input())
    if n == 2:
        print("NO")
    else:
        evu = [i for i in range(1, n+1, 2)]
        oddu = [i for i in range(2, n+1, 2)]
        if sum(evu) + n != sum(oddu):
            diff = (sum(evu) + n) - sum(oddu)
            if diff in oddu:
                print("NO")
            else:
                oddu[-1] += diff  
                if sum(evu) + n == sum(oddu):
                    print("YES")
                    combined_list = evu + oddu
                    print(' '.join(map(str, combined_list)))
                else:
                    print("NO")
        else:
            print("YES")
            combined_list = evu + oddu
            print(' '.join(map(str, combined_list)))
