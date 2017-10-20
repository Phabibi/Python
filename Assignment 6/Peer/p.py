# Own question
# Upper Fruit
# Parsa habibi

def Upperfruit(st):
    i=0
    n=''
    count=0
    while i<len(st):
        if st[i].isalpha():
            if st[i].isupper():
                n=n+len(st[i])*"orange"+" "
                count+=1
        i+=1
         
    if count==0:
        res="No fruits available"
    else:
        res=n
       
    return res
print(Upperfruit("HesasW23W"))
