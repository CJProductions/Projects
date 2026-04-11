def main():  # Main function where the code is run
    valid_temp = False
    while not valid_temp:  # Looops the code until valid_temp = True
        try:  # Continues the loop until a valid temperature is inputted
            temp = float(input("Enter a temperature in celsius"))
            print("Thanks")
            valid_temp = True  # Breaks out of the loop 
        except ValueError:  # If the input is not a number it will loop the code
            print("Invalid input")
    temp_in_fahrenheit = ((9/5) * temp + 32)  # Calculates the temperature in fahrenheit
    print(f"Your temperature in fahrenheit is {temp_in_fahrenheit}")
    exit()
if __name__ == "__main__":
    main()