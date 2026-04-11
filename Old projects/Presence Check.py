def main():  # Main function where the code is run
    valid_name = False  # At the start of the program this is set to false by default
    while valid_name == False:  # Loops until valid_name becomes true
        print("Enter your name: ")  # Asks the user to input their name
        name = input()   # Stores the user's input
        if name != "":  # Checks if the user inputted something
            print("Well done")
            valid_name = True  # If something is inputted then it will set valid_name to true and break out the loop
        else:  # If nothing is inputted it will tell the user to try again
            print("Nothing entered. Try again")
            
            

if __name__ == "__main__":
    main()