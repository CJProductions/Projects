def addcar(parking, max, car):

    if len(parking) >= max:
        print("Full")
    else:
        print("What is your name?")
        name = input()
        print("What is the make of your car")
        make = input()
        print("What colour is your car?")
        colour = input()
        print("What is your car's registration")
        reg = input()
        car = [name, make, colour, reg]
        parking.append(car)
        return parking

def removecar(parking):
    print("Input license plate of car")
    reg = input()
    for i in len(range(parking)):
        try:
            pass
        except:
               pass
def checkparking(parking):
    pass
def closingtime(parking):
    parking.clear()
    print(parking)
    print("Everyone is out now")

def admin(parking, max):
    print("Please enter the number of parking space you would like")
    max = int(input())

    return parking, max

def main():
    parking=[]
    car = ""
    max=6
    exit = False

    print("Welcome to the car park")
    while exit == False:

        print("1. Add car")
        print("2. Remove car")
        print("3. Check parking")
        print("4. Closing time (Boot everyone out)")
        print("5. Admin panel")
        print("6. Exit the program")

        choice = int(input("Select option"))

        if choice == 1:
            parking = addcar(parking, max, car)
        elif choice == 2:
            parking = removecar(parking)
        elif choice == 3:
            print(parking)
        elif choice == 4:
            closingtime(parking)
        elif choice == 5:
            admin(parking, max)
        elif choice == 6:
            exit = True
        else:
            print("Invalid choice")



#Welcome to the carpark simulator
#You have 6 parking spaces in your car park
#you need to make each subroutine work to add, remove, view (check) and empty out the carpark of 6 spaces
#build a main menu in main which allows you to access each of the subroutines, passing parameters.
#make sure to be robust, make sure to use parameter passing and returns (capture them into a variable)



if __name__ == "__main__":
    main()