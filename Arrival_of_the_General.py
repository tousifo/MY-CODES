def equ(listu):
    maxi = max(listu)
    maxi_i = listu.index(maxi)

    minu = min(listu)
    min_i = len(listu) - 1 - listu[::-1].index(minu)

    swaps_to_front = maxi_i
    swaps_to_end = (len(listu) - 1 - min_i)
    

    if maxi_i > min_i:
        count = swaps_to_front + swaps_to_end - 1
    else:
        count = swaps_to_front + swaps_to_end
    
    return count


n = int(input())
listu = list(map(int, input().split()))


print(equ(listu))
