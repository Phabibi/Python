 #############################
#       DESCRIPTION           #
 #############################

 ################################################
# Name: Parsa Habibi                             #
# Class: CMPT-120                                #
# Project: Final Assignment(Flipping Dance Game) #
# Last updated: 2016-08-4                        #
# Hours spent= 10 hours+                         # 
 ################################################

# # # Functions # # #

def matrix(n):
    global list_org
    import random as r
    list_org = [[r.randint(0,1) for x in range(n)] for y in range(n)]
    return  list_org
    

def printtable(alist,size):
    
    print("\n")      
    for i in range(size):
        print("\tcol",i,end="")
    print("\n")
    for i in range(len(alist)):
        print("row",(i),"  ",end="")
        for r in range (len(alist[0])):
            listb = alist[i][r] 
            print(str(listb),end=" \t")
        print ("\n")
    return 
    

def welcome():
    print(  '''Welcome to the "Flipping Dance" game 
 =====================================
 

 Note: Levels 1, 2 and 3 are implemented;
       You will be able to choose your preferred level for each game;
       The digit/color you choose only affects the totals but not flips

       ''')
    return

def rangeofxy (size):
    
    global rangexy
    rangexy = []
    for s in range (size) :
        rangexy.append(s)
    rangexy.append(99)
    return rangexy

def valueofxy (lista , size) :
    global x
    global y
    print ("User, what position are you choosing to flip? (max flips =" +str(size)+ ")\n(Type  99   for both row and column, if you do not want to do more flips) \n")
    x = input(" row?"+"  (<="+ str(size - 1) + ":)")
    while (not x.isdigit()) or (int(x) not in rangexy):
        if not x.isdigit():
            x = input("The value should only have digits, please re-enter \n rows?"+"  (<="+ str(size - 1) + ":)")
        if int(x) not in rangexy :
            x = input("That is not a valid input, please re-enter \n rows?"+"  (<="+ str(size - 1) + ":)")
    y = input(" col?"+"  (<="+ str(size - 1) + ":)")
    while (not y.isdigit()) or (int(y) not in rangexy):
        if not y.isdigit():
            y = input("The value should only have digits, please re-enter \n rows?"+"  (<="+ str(size - 1) + ":)")
        if int(y) not in rangexy :
            y = input("That is not a valid input, please re-enter \n rows?"+"  (<="+ str(size - 1) + ":)")
        
    x = int(x)
    y = int(y)
    

    return x and y 
    

def level1(size,color,level):
    i = 0
    print("The board is \n ================================================= \n ")
    print(" (initial board) ")
    printtable(matrix(size),size)
    rangeofxy(size)


    while i < size :
        valueofxy(list_org , size)

        if x == 99 and y == 99 :
            print ( "This game is over because you did not want to flip again !")
            print (" ")
            return list_org    


        list_org[x][y] = 1 - list_org[x][y]
        print(" The board is \n ---------------- \n \n (after user played ("+ str(x) +"," + str(y) + "))")
        printtable( list_org , size )
        i = i + 1
        
    print ( "This game is over because you reached the maximum allowed flips!")
    
    return list_org


def winning(lista , color ):
    countcols = 0
    countrows = 0
    pointscols = 0
    pointsrows = 0
    global wins
    wins = 0
    
        
    print( "Rows that have an even number of user digit's ("+ str(color) +")")
    for i in range (len(lista)):
        countrows = 0
        for r in range (len(lista[0])):
            if lista[i][r] == color :
                countrows = countrows + 1
        if countrows % 2 == 0 :
            print ("- Row " + str (i)+ "\n" )
            pointsrows = pointsrows + 1
    if pointsrows == 0 :
        print ("-  None of the Rows \n")
        

    print( "Cols that have an even number of user digit's ("+ str(color) +")")
            
    for i in range (len(lista)):
        countcols = 0
        for r in range (len(lista[0])):
            if lista[r][i] == color :
                countcols = countcols + 1
        if countcols % 2 == 0 :
            print ("- Col " + str (i) + "\n")
            pointscols = pointscols + 1
    if pointscols == 0 :
        print ("-  None of the Cols \n")


    if (pointsrows == 0) or (pointscols == 0) :
        print ( "Sorry!  for you to win, the board had to have at least \n one row and one col with an even number of your digit \n but such is not the case; You had chosen digit(" + str(color) +"\n Therefore, I, the computer, win this game!")

    else :
        wins = 1
        print ("Congratulations! you won this game! \n You had chosen digit(" + str(color) +")\n")
        print ("!!! Therefore, this game gives you:" + str(pointsrows+pointscols) + " points!!!")

    

def computer (lista):
    import random as r
    global a
    global b
    a = r.randint(0 , (len(lista)-1))
    b = r.randint(0 , len(lista[0])-1)
    return a and b 

def level2(size ,color , level):
    i = 0
    print("The board is \n ================================================= \n ")
    print(" (initial board) ")
    printtable(matrix(size),size)
    rangeofxy(size)


    while i < size :
        valueofxy(list_org , size)

        if x == 99 and y == 99 :
            print ( "This game is over because you did not want to flip again !")
            print (" ")
            return list_org    

        print(" The board is \n ---------------- \n \n (after user played ("+ str(x) +"," + str(y) + "))")
        x_0 = x
        y_0 = y
        list_org[x][y] = 1 - list_org[x][y]
        while x_0 < len(list_org):
            list_org[x_0][y] = 1 - list_org[x_0][y]
            
            x_0 = x_0 + 1
        while y_0 < len(list_org[0]):
            list_org[x][y_0] = 1 - list_org[x][y_0]
            y_0 = y_0 + 1
        
        printtable( list_org , size )


        computer ( list_org )
        print ("\n NOW ... The computer played... ("+str(a)+","+str(b)+")\n")
        
        print(" The board is \n ---------------- \n \n (after computer played ("+ str(a) +"," + str(b) + "))")

        a_0 = a
        b_0 = b
        list_org[a][b] = 1 - list_org[a][b]
        while a_0 < len(list_org):
            list_org[a_0][b] = 1 - list_org[a_0][b]
            a_0 = a_0 + 1
        while b_0 < len(list_org[0]):
            list_org[a][b_0] = 1 - list_org[a][b_0]
            b_0 = b_0 + 1
        
        printtable (list_org,size)
        i = i + 1
        
    print ( "This game is over because you reached the maximum allowed flips!")
    
    return list_org

def level3(size , color , level):
    i = 0
    print("The board is \n ================================================= \n ")
    print(" (initial board) ")
    printtable(matrix(size),size)
    rangeofxy(size)
    otherside = 1 - color


    while i < size :
        valueofxy(list_org , size)

        if x == 99 and y == 99 :
            print ( "This game is over because you did not want to flip again !")
            print (" ")
            return list_org   



        while list_org[x][y] == otherside :
            print ("User, you are supposed to pick a position with your own color. \n Please provide another position")
            print("")
            valueofxy(list_org , size)
            

         

        print(" The board is \n ---------------- \n \n (after user played ("+ str(x) +"," + str(y) + "))")
        xU = x - 1
        if xU > 0 and xU < size :
            list_org[xU][y] = 1 - list_org[xU][y]
        xD = x + 1
        if xD > 0 and xD < size :
            list_org[xD][y] = 1 - list_org[xD][y]
        yL = y - 1
        if yL > 0 and yL < size :
            list_org[x][yL] = 1 - list_org[x][yL]
        yR = y + 1
        if yR > 0 and yR < size:
            list_org[x][yR] =1 - list_org[x][yR]
               
        list_org[x][y] = 1 - list_org[x][y]
        
        printtable( list_org , size )


        computer ( list_org )
        while list_org[a][b] == color :
            computer ( list_org )
            
        print ("\n NOW ... The computer played... ("+str(a)+","+str(b)+")\n")
        
        print(" The board is \n ---------------- \n \n (after computer played ("+ str(a) +"," + str(b) + "))")

        aU = a - 1
        if aU > 0 and aU < size :
            list_org[aU][b] = 1 - list_org[aU][b]
        aD = a + 1
        if aD > 0 and aD < size :
            list_org[aD][b] = 1 - list_org[aD][b]
        bL = b - 1
        if bL > 0 and bL < size :
            list_org[a][bL] = 1 - list_org[a][bL]
        bR = b + 1
        if bR > 0 and bR < size:
            list_org[a][bR] =1 - list_org[a][bR]
               
        list_org[a][b] = 1 - list_org[a][b]
        
        
        printtable (list_org,size)
        i = i + 1
        
    print ( "This game is over because you reached the maximum allowed flips!")
    
    return list_org
    


def convert_2_to_10 (list_org):
    answer = 0
    r = (len(list_org[0])-1)
    while r > 0:
        for i in range (len(list_org[0])):
            answer = answer + (list_org[0][i] * (2**r))
            r = r - 1
    return answer

def evellevel():
    global level
    level = input("\n Which level would you like to play? \n 1 - Basic , user only, \n 2- Advanced, user and computer, \n 3- Expert, user and computer: ==> ")
    while (not(level.isdigit())) or (level not in ["1","2","3"]) :
        if not(level.isdigit()):
            level = input ("\n The value should only have digits, please re-enter \n Which level would you like to play? \n 1 - Basic , user only, \n 2- Advanced, user and computer, \n 3- Expert, user and computer: ==> ")
        if level not in ["1","2","3"] :
            level = input ("\n That is not a valid input, please re-enter \n Which level would you like to play? \n 1 - Basic , user only, \n 2- Advanced, user and computer, \n 3- Expert, user and computer: ==> ")
    return level

def evelcolor():
    global color
    color = input("\n Which digit/color would you like for you? \n 0 - white, \n 1 - black: ==> ")
    while (not(color.isdigit())) or (color not in ("0" , "1")):
        if not color.isdigit() :
            color = input("\n The value should only have digits, please re-enter \n Which digit/color would you like for you? \n 0 - white, \n 1 - black: ==> ")
        if color not in ("0" , "1") :
            color = input("\n That is not a valid input, please re-enter \n Which digit/color would you like for you? \n 0 - white, \n 1 - black: ==>")
    return color

def evelsize():
    global size
    size = input("\n Size of the board (between 3 and 6 inclusive):")
    while (not(size.isdigit())) or (size not in ["3","4","5","6"]):
        if not(size.isdigit()):
            size = input ("\n The value should only have digits, please re-enter \n Size of board (between 3 and 6 inclusive): ==> ")
        if size not in ["3","4","5","6"] :
            size = input("\n That is not a valid input, please re-enter \n Size of board (between 3 and 6 inclusive): ==>  ")
    return size

def chooselevel(level):
    if level == "1" :
        winning( level1(int(size),int(color),int(level)),int(color))
    if level == "2" :
        winning( level2(int(size),int(color),int(level)),int(color))
    if level == "3" :
        winning (level3(int(size),int(color),int(level)),int(color))
    return
    
    
            

####################### top level ######################################

welcome()
reply = input (" Would  you like to play? (y/n): ==> ")
games = 0
finalreply = "y"
totalwins = 0

while finalreply == "y" :    

    while reply not in ("y" , "n") :
        reply = input(" That is not a valid input, please re-enter \n Would  you like to play? (y/n): ==> ")
        
    finalreply = "n"
    if reply == "y" :

        evellevel()
        evelcolor()
        evelsize()

        chooselevel(level)
        totalwins = totalwins + wins
        finalreply = input ("Would  you like to play again? (y/n): ==> ")

        while finalreply not in ("y" , "n"):
            finalreply = input(" \n That is not a valid input, please re-enter \n Would  you like to play? (y/n): ==> ")
        games = games + 1

    if reply == "n":
        games = 0

if games >= 1:
    print ("\nTOTALS ALL GAMES ")
    print ("Total points user in all games:" + str(games) )
    print ("Total games the user won: " + str(totalwins))
    print ("Total games the computer won:" + str(games - totalwins))
    print ( "Board value  of last board's first row in decimal:" + str(convert_2_to_10 (list_org)))
    
    
else:        
    print ( "/n Too bad that you did not want to play at all! Bye!")


