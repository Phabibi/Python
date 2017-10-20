# Assignment 6 C
# Count Lower
# Parsa Habibi

def  countLowerFromUntil(st,start):
    i=start
    total=0

    while i<len(st) and not(st[i].isdigit()):
        if st[i].isalpha():
            if st[i].islower():
                total=total+1
        i=i+1

    return total 

print(countLowerFromUntil("1ABCxAxx",4))
