# Assigment peer

def replaceeven(st):
    i=0
    n=""
    while i<len(st):
        if st[i].isdigit():
            if int(st[i])%2==0:
                t=len(st[i])*'%'
                z=st[:i]+t+st[i+1:]
                n+=z
        i+=1
    return n

string="abc123cdf"
print (replaceeven(string))
