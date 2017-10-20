# Assigment 6
# Peer A *Upper
# Parsa Habibi

def UpperLetters (st):
    i=0
    res=0
    while i<len(st):
        if st[i].isalpha():
            if st[i].isupper():
                res=res+1
        i+=1
    if res==0:
        res1="nothing"
    else:
        res1=res
    return res1
        
print(UpperLetters(""))
