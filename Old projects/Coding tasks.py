def billSplit():
    #Asks the user how much the bill is
    print("Input how much the bill is in £00.00")
    bill = float(input())
    #If the bill isn't 0 then the bill isn't fully paid
    while bill != 0:
        #Repeatedly asks how much people are chipping in
        print("Please input how much you will chip in")
        amount = float(input())
        bill = bill - amount
        print("You still have", bill, "left")


    print("Bill has been paid")
def secret():
    #Asks the user to input the secret password
    print("Please input secret password")
    password = input()
    #If they put in the correct password then they will be welcomed to nothing
    if password == "secret":
        print("Welcome")
    #Otherwise they will be yelled at
    else:
        print("Not Welcome!!!")

def carRental():
    print("Car hiring service")

    # Asks the user for the number of days they will be hiring the car for
    daysHired = int(input("How many days are you hiring? "))

    # If they input less than a day they will be asked to try again
    while daysHired < 1:
        print("Car hires are 1 day at the minimum. Please retry")
        daysHired = int(input("How many days are you hiring?"))

    # Asks the user how many miles are on the car before it's driven
    initialMiles = int(input("How many miles are clocked before hiring"))

    # Asks the user how many miles are clocked after
    endMiles = int(input("How many miles are clocked after hiring?"))

    # Calculates the miles after the hire
    totalMiles = endMiles - initialMiles

    # Calculates how much the days and miles would cost
    daysCharged = daysHired * 20
    milesCharged = totalMiles * 0.05

    # Outputs the total charged to the user
    totalCharged = daysCharged + milesCharged
    print("Your total charge is:", totalCharged)

def main():
    #Asks the user what subroutine they want to use
    print("Select which thing you want")

    print("Press 1 to go to the secret password")
    print("Press 2 to go to the car hire calculator")
    print("Press 3 to go split the bill")
    thingPicked = int(input())

    if thingPicked == 1:
        secret()
    elif thingPicked == 2:
        carRental()
    elif thingPicked == 3:
        billSplit()

if __name__ == '__main__':
    main()