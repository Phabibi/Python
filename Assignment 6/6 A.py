 # Assignment 6 A
# Pairs
# Parsa Habibi

def immPairs(st):
    n=True
    i=0
    while i in range(len(st)):
        i=i+1
        if i<len(st):
            if st[i-1]==st[i+1]: 
                n=n
            else:
                n=not(n)
    return n
print(immPairs("cfx"))
    
            

