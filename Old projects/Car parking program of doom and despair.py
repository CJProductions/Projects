def addcar(parking, max):
    if len(parking) >= max:
        print("Full")
        return parking
    else:
        name = input("Input name of car owner")
        reg = input("Input license plate registration")
        colour = input("Input colour of the car")
        model = input("Input make of the car")
        car = [name, reg, colour, model]
        parking.append(car)
        return parking
def removecar(parking):
    print("Enter the registration of the car")
    reg = input()
    for i in range(len(parking)):
        try:
            parking[i].index(reg)
            parking.pop(i)
            print(parking)
        except:
                pass

    return parking
def checkparking(parking):
    print(parking)
def closingtime(parking):
    parking.clear()
    print(parking)
    print("Everyone is out now")
def admin(parking, max):
    pass

def main():
    parking=[]
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
            parking = addcar(parking, max)
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
#you need to make each subroutine work to add, remove, view (check) and empty out the carpark of 6 spaces/
#build a main menu in main which allows you to access each of the subroutines, passing parameters./
#make sure to be robust, make sure to use parameter passing and returns (capture them into a variable)
#Add functionality to your car park program by storing the make, colour, owner and number plate of the cars
#Add an admin functionality to the car park program to add an admin function that will change what the max number of cars is and to allow them to search for a car by owner or number plate
#Add your own functionality to either of these programs!


if __name__ == "__main__":
    main()