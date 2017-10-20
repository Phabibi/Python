# Parsa Habibi
# avg odd


def avgOfOdds(st):
    i=0
    n=0.0
    res=0
    while i<len(st):
        if st[i].isdigit():
            if int(st[i])%2==1:
                n=n+int(st[i])
                res=res+1
        i+=1
    if res==0:
        res1=0.0
    else:
        res1=n/res
    return res1
print(avgOfOdds("A3JD7DJ4"))

