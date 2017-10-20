# BONUS

def acgBackw(st):
    sum=0.0
    n=0
    i=len(st)-1

    while (i>=0 and not(st[i].isalpha())):
        if st[i].isdigit():
            sum+=1
            n+=1

        i+=1

    if n==0:
        res=0.0

    else:
        res=sum/n

    return res
        
            
