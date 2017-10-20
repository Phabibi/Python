# Assignment 4.1 H
# Repeat Middle
# Parsa Habibi

def repeat_middle(string):
    if len(string)%2==0:
        return '!!'+string[int((len(string)/2)-1):int(((len(string)/2)+1))]*len(string)+'!!'
    else:
        return '!'+string[int(len(string)//2)]*len(string)+'!'

print (repeat_middle("abMNcd"))
