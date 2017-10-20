def findUpper(st):
    i=0
    res=0
    while i<len(st):
        if st[i].isalpha():
           if st[i].isupper():
               res+=1+len(st[i])
        i+=1
    return res

print(findUpper("ABsC"))
