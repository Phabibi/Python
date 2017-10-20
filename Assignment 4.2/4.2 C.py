# Assignment 4.2 C
# Digit Plus
# Parsa Habibi

def digits_plus(dig):
    res=''
    for i in range(0, dig+1):
        res=res+str(i)+'+'
    return res
print (digits_plus(3))
