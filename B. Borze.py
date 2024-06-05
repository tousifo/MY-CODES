code = input().strip()
deco = ""

for i in range(len(code)):
    if code[i] == '.':
        deco +='0'
        i+=1
    elif code[i] == '-':
        if code[i+1] == '.':
            deco += '1'
            i+=2
        elif code[i+1] == '-':
            deco += '2'
            i+=2
            
print(deco)                
        