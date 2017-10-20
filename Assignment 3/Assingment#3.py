
###############################
#       DESCRIPTION           #
###############################

# Name: Parsa Habibi #
# Class: CMPT 120 ##########
# Student number: 301262132 ###
# Project: Password Generator #  
# Last update: 2016-06-6  ############################ 
# Hours spent : atleast 30 mins everyday (total=3 hrs)##################################################################
# My program will generate a unique and cryptic password based on the information the user gives (name,lastname,age...)#
#     The program will also includes TRACE PROMPTS which calculate users square root of his/her age and calculate ######
#     exactly how many letters the password have based on information given by user.                  #############
#                                                                                                     #
#######################################################################################################


import math 

# # # Welcome Message # # # 

def Welcome_message():
    print('Welcome to CMPT 120 Password genrator.')
    print('Please follow the system promts')
    print('\n')
    return

# # # variables # # #
Welcome_message() 

Name, Lastname=input('''Please type your first and last name
(separated with a space):''').split()
print('\n')

age=int(input("Please emter your age:"))
print('\n')

Course, Number=input('''Please type the name of one course,
(first and second part separated by a dash) (-): ''' ).split("-")
print('\n')


print('Processing...')
print('\n')

Square_root_age=math.sqrt(age)

print(' Trace-square root of age=',Square_root_age)
print('\n')

# # # Calculations # # #

Password_1=Name[1].upper()                           
Password_2=Lastname[0].upper()
Password_2nd=Lastname[1]
Password_3=Lastname[len(Lastname)-1]
Password_4=age//10
Password_5=int(Square_root_age)
Password_6=Course[len(Course)-1]

 # # # Result # # #
 
if (Number).isdigit():
    Password_7=Number[len(Number)-1]
    PASSWORD=(Password_1+Password_2+Password_2nd+Password_3+(Password_4*"*")+(Password_5*"$")+Password_6+Password_7)

else :
    Password_7 = None
    PASSWORD=(Password_1+Password_2+Password_2nd+Password_3+(Password_4*"*")+(Password_5*"$")+Password_6)
    

if (len(PASSWORD))%2 == 0:
    Password_8="E"
    PASSWORD=PASSWORD+Password_8
    
print(PASSWORD)

# # # END OF THE PROGRAM


