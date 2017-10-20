# Assigment 6
# Peer * expOff
# Parsa Habibi

def expOfFirst(st):
    i=0
    n=0
    res=0
    res1=0
    res2=0
    count1=0
    count=0
   

    while i<len(st):
        if st[i].isdigit():
            n+=len(st[i])
            if n==1:
                res1+=int(st[i])
                count1+=0
            if n==2:
                res2+=res1**int(st[i])
                count+=1
        i+=1

        if count==0 and count1==0:
            final="Not enough digits!"
        else:
            final=res2

    return final

print(expOfFirst("abd2uk*"))
