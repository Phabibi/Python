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
    global Matrix
    import random as r
    Matrix=lista=[[r.randint(0,1) for x in range(n)] for y in range(n)]
    
    return Matrix
def range_of_xy(size):
    global rangexy

    rangexy=[]
    for i in range(size):
        rangexy.append(i)
    rangexy.append(99)
    return rangexy

def table(alist,size):

    print("\n")
    
    for i in range(size):
        print(" "*6+"col",i,end="")
    print("\n")
    for i in range(len(alist)):
        print("row",(i),"  ",end="")
        for r in range (len(alist[0])):
            listb = alist[i][r] 
            print(str(listb),end="          ")
        print ("\n")
    return

    
def winning(lista , color ):
    countcols = 0
    countrows = 0
    pointscols = 0
    pointsrows = 0
    
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
        print ("Congratulations! you won this game! \n You had chosen digit(" + str(color) +")\n")
        print ("")
        print ("!!! Therefore, this game gives you:" + str(pointsrows+pointscols) + " points!!!")


def flip(color):
    
    global Colors

    if color=="1":
        Colors="0"
    if coloe=="0":
        Colors="1"
    return Colors
    
def value_of_xy(lista,size):
    
    global x
    global y
    
    print ("User, what position are you choosing to flip? (max flips =" +str(size)+ ")\n(Type  99   for both row and column, if you do not want to do more flips)")
    x= input("row?"+"(<="+ str(size - 1) + "): ")
    while(not x.isdigit()) or (int(x) not in rangexy):
        if not(x.isdigit()):
             x=input("The value should only have digits, please re-enter: ")
        if int(x) not in rangexy:
             x=input("That is not a valid input, please re-enter: ")
             
    y=(input("col?"+"(<="+ str(size - 1) + "): "))
    while(not y.isdigit()) or (int(y) not in rangexy):
                if not(y.isdigit()):
                    y=input("The value should only have digits, please re-enter: ")
                if int(y) not in rangexy:
                    x=input("That is not a valid input, please re-enter: ")
    x=int(x)
    y=int(y)
        
    return x and y

'''
def level_1(size,color,level):
    i=0
    print( 
The board is
-------------

(initial board)
    )
        
    while x == 99 and y == 99 :
        print ( "This game is over because you did not want to flip again !")
        print (" ")
        return Matrix
    
            
         
         Matrix[x][y]=1-Matrix[x][y]
         print(" The board is \n ---------------- \n \n (after user played ("+ str(x)+","+str(y)+ "))")

         table( Matrix , size )
         i = i + 1

    return winning(Matrix,color)

'''     
    

# # # Top Level # # #  
    

def welcome():
        print(  '''Welcome to the "Flipping Dance" game 
 =====================================
 

 Note: Levels 1, 2 and 3 are implemented;
       You will be able to choose your preferred level for each game;
       The digit/color you choose only affects the totals but not flips

       ''')
   
   
        return
#  #  # Top Level # # #

reply=input("Would  you like to play? (y/n): ==> ")

game=0
finalreply="y"
totalwins=0

while finalreply=="y":
    reply=finalreply
    while reply not in ("y","n"):
            reply=input("That is not a valid input, please re-enter: ")
    if reply=="y":
        print("\n")
        welcome()
        
        level=input("Which level would you like to play? \n 1 - Basic , user only, \n 2- Advanced, user and computer, \n 3- Expert, user and computer :")
        while (not(level.isdigit())) or (level not in['1','2','3']):
            if level not in ('1','2','3'):
                level=input('That is not a valid input, please re-enter: ')
            if (not level.isdigit()):
                level=input('The value should only have digits, please re-enter: ')
    
    
        color=input('''Which digit/color would you like for you?
 0 - white,

 1 - black: ==> ''')

        while (not(color.isdigit())) or (color not in['0','1']):
            if not(color.isdigit()):
                color=input('\n The value should only have digits, please re-enter:  ')
            if color not in('0','1'):
                color=input(' \n The value should only have digits, please re-enter: ')
        

 
        size=input("Size of board (between 3 and 6 inclusive): ==> ")
        while (not(size.isdigit())) or (size not in['3','4','5','6']):
            if not(size.isdigit()):
                size=input('\n The value should only have digits, please re-enter: ')
            if size not in['3','4','5','6'] and (not size.isdigit()):
                size=input('\n The value should only have digits, please re-enter: ')
            
        print("\n")
   
        if level == "1" :
            winning( level1(int(size),int(color),int(level)),int(color))
        if level == "2" :
            winning( level2(int(size),int(color),int(level)),int(color))
        if level == "3" :
            winning (level3(int(size),int(color),int(level)),int(color))
        finalreply = input ("Would  you like to play again? (y/n): ==> ")
        games = games + 1

        
    if reply == "n":
        games = 0

while games >= 1:
    print ("TOTALS ALL GAMES ")
    print ("Total points user in all games:" + str(games) )
    print ("Total games the user won: " + str(totalwins))
    print ("Total games the computer won:" + str(games - totalwins))
    print ( "Board value  of last board's first row in decimal:" + str(convert_2_to_10 (list_org)))
    break
    

else:        
    print ( "Too bad that you did not want to play at all! Bye!")


