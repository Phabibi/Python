# Apples
# Parsa habibi

def apple(st):
    i=0
    n=0
    count=0

    while i<len(st):
        if st[i].isalpha():
            n+=len(st[i])
            count+=1
        i+=1

        if count!=1:
            res="there are "+str(n)+" apple(s)"

    return res
val = apple ("-------ab------")
print (val)
