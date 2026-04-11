def main():
    
    valid = False
    valid_name = False
    valid_number = False
    valid_postcode = False
    
    while not valid:
        
        while not valid_name:
            
            name = input("What is your name?: ")
            if name != "":
                print("Valid name inputted")
                valid_name = True
            else:
                print("Nothing entered")
            
        while not valid_number:
            
            try:
                phone_number = input("What is your phone number?: ")
                valid_number = True
            except ValueError:
                print("Invalid number")
                
        while not valid_postcode:
            
            postcode = input("What is your postcode?: ")
            if len(postcode) == 8:
                print("Valid postcode")
                valid_postcode = True
            else:
                ("Invalid postcode")
        valid = True

    print(name, phone_number, postcode)
if __name__ == "__main__":
    main()