def main():

    carsize = 0
    print("Theme park height checker")

    while carsize != 8:
        height = int(input("How tall is the rider"))
        if height >= 140:
            print("hop on")
            carsize += 1
            print("Number of riders is",carsize)
        else:
            #Asks the user if the rider is going with an adult
            adult = input("Is the rider going with an adult? yes/no")

            if adult == "yes":
                print("hop on fr")
                carsize +=2
                print("Number of riders is", carsize)
            elif adult == "no":
                print("Sorry lil bro")
            else:
                print("Invalid input or smth")

    else:
        print("Car is now full")



if __name__ == "__main__":
    main()