# Assignment 6 D
# Count Lower
# Parsa Habibi

def countLower(st):
    i=0
    res=0
    while i<len(st):
        
        if st[i].islower():
            res+=1

        i+=1
    return res

val = countLower("a1a2a3AAAa")
print(val)

