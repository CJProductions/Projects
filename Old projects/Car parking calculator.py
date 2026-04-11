def main():
    print("Car park")

    #get car registration from the user
    print("Enter registration")
    carReg = input()

    #validation of number plate
    while len(carReg) > 8 or carReg == "":
        print("Invalid Registration. Enter registration again.")
        carReg = input()

    #get car registration from the user
    print("Enter length of stay")
    lengthOfStay = int(input())

    #validation of number plate
    while lengthOfStay <= 0 or lengthOfStay > 24:
        print("Invalid length of stay. Enter length of stay... again.")
        lengthOfStay = int(input())

    #Check to see how long they have been staying
    if lengthOfStay <= 2:
        charge = 0.5 * lengthOfStay
    else:
        charge = 2 * lengthOfStay
    #outputs final charge
    print("Your final charge is: £",charge)
if __name__ == "__main__":
        main()