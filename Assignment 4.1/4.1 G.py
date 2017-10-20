# Assignment 4.1 G
# Food clock
# Parsa Habibi

def food(time,sweets):
    time=int(time)
    if time<6:
        return "no food"
    if 6<=time<=10:
        "breakfast"
        if sweets==True:
            return "breakfast,marmalade"
        else:
            return "breakfast,coffee"
    if 11<=time<=15:
        "lunch"
        if sweets==True:
            return "lunch,dessert"
        else:
            return "lunch"
    if 15<=time<=22:
        "dinner"
        if sweets==True:
            return "dinner,dessert"
        else:
            return "dinner"
    if time>22:
        return "no food"

print (food(7,True))



