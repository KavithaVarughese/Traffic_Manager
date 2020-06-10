# Traffic Manager
#Input 1 - Density of Each Traffic Route
#Input 2 - Time taken for the ready area for each route to clear. (Only required for scenario 2)
#           In reality, you get it from the GPS of car to the sensors installed at signals using vanet network
#In this algorithm, we return the waiting time for a vehicle waiting in between signal and point A according to question.
#Input 3 - Route where your vehicle is waiting
       


import sys

#Traffic routes according to phases
Routes_Dictionary = {1:[5,6], 2:[5,6], 3:[7,8], 4:[7,8], 5:[1,2], 6:[1,2], 7:[3,4], 8:[3,4]}


def Scenario1(Density_Dictionary,route):
    copy = Density_Dictionary
    Time = 60

    waiting_time = 0

    while True:
        j = max(copy, key=copy.get)
        i1, i2 = Routes_Dictionary[j]
        if copy[i1]>copy[i2]:
            i = i1
        else:
            i = i2

        if (i == route) or (j == route):
            break

        waiting_time = waiting_time + Time
        copy[i] = 0
        copy[j] = 0

    print("waiting time is \n")    
    print(waiting_time)
            

        


def Scenario2HighPriority(Density_Dictionary, Time_Dictionary,route):
    copy_d = Density_Dictionary
    copy_t = Time_Dictionary

    waiting_time = 0

    while True:
        j = max(copy_d, key=copy_d.get)
        i1, i2 = Routes_Dictionary[j]
        if copy_d[i1]>copy_d[i2]:
            i = i1
        else:
            i = i2

        if (i == route) or (j == route):
            break
        
        #schedule function
        Time = max(copy_t[j], copy_t[i])

        waiting_time = waiting_time + Time
        copy_d[i] = 0
        copy_d[j] = 0
        copy_t[i] = 0
        copy_t[j] = 0

    print("waiting time is \n")    
    print(waiting_time)


def Scenario2LowPriority(Density_Dictionary, Time_Dictionary,route):
    copy_d = Density_Dictionary
    copy_t = Time_Dictionary

    waiting_time = 0

    while True:
        j = min(copy_d, key=copy_d.get)
        i1, i2 = Routes_Dictionary[j]
        if copy_d[i1]<copy_d[i2]:
            i = i1
        else:
            i = i2

        if (i == route) or (j == route):
            break
        
        #schedule function
        Time = max(copy_t[j], copy_t[i])

        waiting_time = waiting_time + Time
        copy_d[i] = sys.maxsize
        copy_d[j] = sys.maxsize
        copy_t[i] = 0
        copy_t[j] = 0

    print("waiting time is \n")    
    print(waiting_time)


def printMenu():
    print("enter the integer for desired function\n")
    print("1 - Scenario 1\n")
    print("2 - Scenario 2 High Priority\n")
    print("3 - Scenario 2 Low Priority\n")
    print("4 - Change Density and Time Values\n")
    print("5 - Quit\n")


from collections import defaultdict 


Density_Dictionary = {}

Time_Dictionary = {}
print("Enter the densities of the traffic routes from 1 to 8")

for x in range(8):
    Density_Dictionary[x+1] = int(input())

print("Enter the times of the traffic routes from 1 to 8")
for x in range(8):
    Time_Dictionary[x+1] = int(input())

printMenu()

print("Enter choice")
choice = int(input())

while(choice != 5):

    if choice == 1:
        print("Enter route")
        route = int(input())
        Scenario1(Density_Dictionary,route)
    elif choice == 2:
        print("Enter route")
        route = int(input())
        Scenario2HighPriority(Density_Dictionary,Time_Dictionary,route)
    elif choice == 3:
        print("Enter route")
        route = int(input())
        Scenario2LowPriority(Density_Dictionary,Time_Dictionary,route)
    elif choice == 4:
        print("Please quit program and start again")
    elif choice == 5:
        break
    else :
        print("Wrong option ")
    
    print("\n")
    printMenu()

    print("Enter choice")
    choice = int(input())



print("Goodbye!!!")