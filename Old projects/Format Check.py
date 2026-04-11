import re

def main():
    valid_email = False
    while not valid_email:
        email = input("Enter your email: ")
        if re.search(".co.uk$", email):
            print("Valid UK email")
            valid_email = True
        else:
            print("Invalid UK email address, try again")

if __name__ == "__main__":
    main()