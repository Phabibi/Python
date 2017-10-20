# Assignment 6 B
# Avarage Odd
# Parsa Habibi

def avgOdd(st):
    n=0.0
    i=0
    
    while i<len(st):
        if st[i].isdigit():
            if int(st[i])%2!=0:
                n=n+((int(st[i]))//(n+len(st[i])))
        i+=1
    return n
print(avgOdd("---"))
