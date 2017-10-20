# Assigment 6
# Peer A *LOwer
# Parsa Habibi

def countLowerLetters(st):
    i=0
    n=""
    res=0
    while i<len(st):
        if st[i].isalpha:
            if st[i].islower():
                n+=st[i]
                res+=1

        i+=1

    if res==0:
        res1="No lowercase letters!"
    else:
        res1=n

    return res1
val=countLowerLetters("abcEFE12")
print(val)
