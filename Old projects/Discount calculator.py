import datetime

def main():

    date = datetime.date.today()
    meal = 10
    drink = 3
    #I don't really need these statements unless I plan on making more "optimal code"
    isStudent = False
    hasDiscount = False
    isSaturday = False

    #Determines if it is saturday when discounts aren't available
    if date.strftime("%A") == "Saturday":
        #If it is saturday then discount cards and student discounts won't be available and will tell the user that discounts aren't available on saturday
        hasDiscount = False
        isStudent = False
        print("No discounts on saturday")
    else:
        print("Discounts are available")
    #Asks the user if the customer has a discount card
    print("Does the customer have a discount?")
    discountOption = input("Press y/n")
    #If the customer has a discount card drinks will cost 1.50 for everyone
    if discountOption == "y":
        drink = 1.5
        hasDiscount = True
        print("Your drink cost is now ", drink)
    elif discountOption == "n":
        print("Drinks still costs", drink)
    else:
        print("Incorrect option please try again")

    print("Is the customer a student?")
    studentOption = input("Press y/n")
    if studentOption == "y":
        isStudent = True
        drink = 2.4
        meal = 8
    elif studentOption == "n":
        print("oh ok then")
    else:
        print("Incorrect option please try again")

    #Not done yet xP




if __name__ == "__main__":
    main()