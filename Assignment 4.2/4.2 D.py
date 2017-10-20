# Assignment 4.2 D
# Add Digits In String
# Parsa Habibi

def addDigitsInString(string):
    res=0
    for i in string:
        if i.isdigit():
            res=res+int(i)
    return res 
total  = addDigitsInString("..1..5..3..")
print (total)
