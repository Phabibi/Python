# Assignment 4.2 F
# Give Me unit Position
# Parsa Habibi

def  giveMeUnitPos(st,ch):
    res=".."
    for i in range(len(st)):
        if ch==st[i]:
            unit=int(i%10)
            res+=str(unit)+".."
    return res
s = "abcdabcdabcdabcd"
c = "a"
print(giveMeUnitPos(s,c))
