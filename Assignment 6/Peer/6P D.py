# Assigment 6
# Peer A *addodds
# Parsa Habibi



def addOddPosition(st):
    i=0
    n=0
    res=0 
    while i<len(st):
        if st[i].isdigit():
            if i%2==1:
                n+=int(st[i])
                res+=1
        i+=1     

    if res==0:
        res1="nothing"
    else:
        res1=n

    return res1 
print(addOddPosition("a1e2r4h5"))
