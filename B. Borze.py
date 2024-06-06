code = input().strip()
deco = ""

i = 0
while i < len(code):
    if code[i] == '.':
        deco += '0'
        i += 1
    elif code[i] == '-':
        if i + 1 < len(code) and code[i + 1] == '.':
            deco += '1'
            i += 2
        elif i + 1 < len(code) and code[i + 1] == '-':
            deco += '2'
            i += 2
            
print(deco)                
        