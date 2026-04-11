def main():
    valid_postcode = False
    while not valid_postcode:
        postcode = input("Enter a Leeds postcode")
        if postcode[0] == "L" and postcode[1] == "S":
            print("Valid Postcode")
            valid_postcode = True
        else:
            print("Not a Leeds postcode")
if __name__ == "__main__":
    main()