# Assignment 4.2 E
# Max Digits
# Parsa Habibi

def maxDigs(dig):
    res=""
    for i in dig:
        if i.isdigit():
            res=res+i
    if res.isdigit():
        res=max(res)
    else:
        res="-1"
    return res
print (maxDigs("a1b9c3!$8"))
