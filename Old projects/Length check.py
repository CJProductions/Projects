def main():  # Main function where the code is run
    valid_number = False
    while not valid_number:  # Loops the code while valid_number is false
        print("Enter your phone number")
        phone_number = input()  # Stores the user's input as phone_number
        if len(phone_number) == 11:  # Checks the length of phone_number to see if it fits the length requirement
            print("Well done")
            valid_number = True  # Sets valid_number to true to break the loop
        else:
            print("Invalid phone number")
    
if __name__ == "__main__":
    main()