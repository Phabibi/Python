###############################
#       DESCRIPTION           #
###############################


###############################################
# Name: Parsa Habibi                          #
# Class: CMPT-120                             #
# Project: Turtle, The Imposible Triangle     #
# Last updated: 2016-07-2                     #
# Hours spent= 6 hours+                       # 
###############################################

# # # Top Level # # # 


import turtle as t
import random as r



# # # Random Funcions # # #

def randomColor():
    red = r.randint(0,255)
    green = r.randint(0,255)
    blue = r.randint(0,255)
    colorToReturn = (red,green,blue)
    return colorToReturn

# # # Main Triangle # # #

def Middle_Triangle():
        t.pensize(4)
        t.fillcolor("black")
        t.begin_fill()
        t.pendown()
        t.fd(120)
        t.penup()
        t.left(180)
        t.fd(60)
        t.right(60)
        t.pendown()
        t.fd(120)
        t.left(180)
        t.penup()
        t.fd(60)
        t.right(60)
        t.pendown()
        t.fd(120)
        t.end_fill()
        return
print(Middle_Triangle())

def Right_Side():
        thick=4
        t.left(120)
        t.fd(240)
        t.left(120)
        t.fd(300)
        t.left(60)
        t.fd(60)
        t.left(120)
        t.fd(240)
        t.penup()
        t.home()
        return
print(Right_Side())

def Bottom():
    t.left(60)
    t.fd(60)
    t.left(60)
    t.fd(60)
    t.left(120)
    t.pendown()
    t.fd(240)
    t.left(120)
    t.fd(280)
    t.left(46)
    t.fd(74)
    t.penup()
    t.home()
    return
print(Bottom())

def Left_Side():
    t.fd(120)
    t.left(120)
    t.fd(240)
    t.left(120)
    t.pendown()
    t.fd(280)
    t.left(46)
    t.fd(74)
    t.penup()
    t.home()
    

    return

print(Left_Side())

# # # Spiral Triangle # # # 

t.speed(100)

def Background(number,angle,path):
    t.speed(1000)
    t.pensize(0.5)
    t.penup()
    t.fd(30)
    t.left(90)
    t.fd(20)
    t.pendown()
    t.right(90)
    for path in range(number):
        t.fd(path)
        t.left(angle)
        t.left(angle)
        t.fd(path)
    return
print(Background(127,60,10))

def Home():
    t.penup()
    t.home()
    return
print(Home())

# # # Dots # # # 

def dots_bottom(distance,width,height):
    t.colormode(255)
    t.pensize(0.5)
    t.penup()
    t.right(90)
    t.fd(60)
    t.left(90)
    t.left(180)
    t.fd(80)
    t.left(180)
    for i in range(height):
        for i in range(width):
            t.dot()
            t.fd(distance)
            t.pencolor(randomColor())
        t.back(distance*width)
        t.right(130)
        t.fd(distance)
        t.left(130)
    return
print(dots_bottom(10,28,6))

def dots_left(distance,width,height):
    t.colormode(255)
    t.pensize(0.5)
    t.penup()
    t.left(90)
    t.fd(15)
    t.right(90)
    t.left(110)
    for i in range(height):
        for i in range(width):
            t.dot()
            t.fd(distance)
            t.pencolor(randomColor())
        t.back(distance*width)
        t.right(50)
        t.fd(distance)
        t.left(50)
    return
print(dots_left(10,6,29))

def dots_right(distance,width,height):
    t.colormode(255)
    t.pensize(0.5)
    t.penup()
    t.fd(50)
    t.right(120)
    
    
    for i in range(height):
        for i in range(width):
            t.dot()
            t.fd(distance)
            t.pencolor(randomColor())
        t.back(distance*width)
        t.right(50)
        t.fd(distance)
        t.left(50)
    return
print(dots_right(10,6,30))

# # # The End # # # 
