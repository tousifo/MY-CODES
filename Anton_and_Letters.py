

unak = input()

if unak=="{}":
    una_setu = set()
else:
    una = [char.strip() for char in unak [1:-1].split(', ')]
    una_setu = set(una)

counta = len(una_setu)


if len(una_setu) == 0 :
    print ("0")
else:
    print (counta)