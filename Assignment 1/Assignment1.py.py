###############################
#       DESCRIPTION           #
###############################

# Name: Parsa Habibi
# Class: CMPT 120
# Student number: 301262132
# Project: Runner Distance Calculator
# Last update: 2016-06-1
# Hours spent : apxr 2 hours
# The program acts as an convertor from different numeric system and will execute the differance between two distances in 2 differant versions

name = input('''Hello!
please enter your name : ''')
print("\n")
(print('''Hello''', name,


       '''Welcome to the CMPT 120 Runner distances system!  
You will be able to calculate the distance between two locations
Please follow the system prompts''' ))
print("-------------------------------------------") #  #  # in order for user to feel more interactive with the program I ask for their name 
print("Please provide the data for the first runner : ")
runner_1_Kilometer=int(input("Number of kilometers (km) = ")) # # # distance covered by the first runner in Km 
runner_1_Meter=int(input("Number of meters (m)  (between 1 to 999) = ")) # # # distance covered by the first runner in M
runner_1_Centemeter=int(input("Number of centemeter (cm) (between 1 to 99) = ")) # # # distance covered by runner in Cm 
print("\n")
print("Thank you" ,name,"please provide data for second runner.")
print("\n")
# # # # now we ask for the data on the second runner
runner_2_Miles=int(input("Number of miles (mi) = "))
runner_2_Yards=int(input("Number of yards (yd) (between 1 and 1759 inclusive = "))
runner_2_Feet=int(input("Number of feet (cm) (between 1 and 2 inclusive) = "))
print("\n")
print("     ","Thanks",name,".","please trace the priting to best follow the executions")
runner_1_in_centemeter=(runner_1_Kilometer * 100000)+(runner_1_Meter * 100)+(runner_1_Centemeter)
print("     ","First runner all in cm = ",runner_1_in_centemeter,"cm")
print("\n")
print("FIRST RESULT: Distance of second runner in ft and in cm: ")
print("---------------------------------------------------------")
runner_2_in_feet=(runner_2_Miles*5280)+(runner_2_Yards*3)+(runner_2_Feet)
print("The second runner all in ft = ",runner_2_in_feet,"(ft)")
print("\n")
runner_2_in_centemeter=runner_2_in_feet*30.48
print("The second runner all in cm (1ft = 30.48 cm) = ",runner_2_in_centemeter,"(cm)")
print("------------------------------------------------------------")
print("\n")
diff_between=(runner_2_in_centemeter)-(runner_1_in_centemeter)
print("SECOND RESULT:  Difference between the two runners in cm = ",abs(diff_between))
print("--------------------------------------------------------------------------")
print("THIRD RESULT:   The difference is also expressible as follows: ")
diff_between_kilometer=(abs(diff_between))//100000
diff_between_meter=(abs(diff_between))//100%1000
diff_between_centemeter=(abs(diff_between))//1%100
print(diff_between_kilometer,"km",diff_between_meter, "m" , abs(diff_between_centemeter),"cm")
print("Thanks for your participation",name,"!")
print("End of the program") 

# # # # End











