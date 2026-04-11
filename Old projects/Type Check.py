def main():  # Main function where the code is run
    valid_temp = False
    while not valid_temp:  # Loops the code until valid_temp = True
        temp = input("Enter a temperature in Celsius:  ")
        if temp.isdigit():  # Checks to see if the string is a number
            valid_temp = True  # Breaks out of the loop
            print("Ok")
        else:  # Otherwise the code keeps looping until a number is inputted
            print("Invalid data entered. Try again")
        

    temp_in_fahrenheit = ((9/5) * int(temp) + 32)  # Converts temp into an integer and then calculates what it'd be in fahrenheit
    print(f"Your temperature in fahrenheit is {temp_in_fahrenheit}")
    
    
if __name__ == "__main__":
    main()