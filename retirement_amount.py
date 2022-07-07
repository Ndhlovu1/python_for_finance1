import numpy as np

#Receive a desired amount you'd like to have when you retire and see how much you need to save

print("**********************************************************************************")

print("Good Day : Welcome to Retirement Planner : Your Friendly Retirement Planner      *")

print("Today we'll help you see how much you need to save in order to reach your goal   *")

print("**********************************************************************************\n")
start = input("Would you like to start? [y/n]\n")

if start == "y":
    amount = int(input("\nEnter your desired amount : \n"))
    rating = float(input("Enter Rate : \n"))
    rates = rating/100
    year = int(input("Enter the years left for you to retire"))

    ret_save = np.pmt(rate = rates/12, nper= year *12, pv=0, fv=amount)
    print("________________________________________________________________________________")
    print("The amount you have to save is : Nad",ret_save,"                             ---")
    print("________________________________________________________________________________")

else:
    quit()


