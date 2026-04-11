def main():
    chkflg = True
    while chkflg:
        try:
            age = int(input("How old are you? "))
        except ValueError:
            print("Please enter a number.")
            continue
        if age >= 18:
            print("You can vote")
            chkflg = False
        elif age == 17:
            print("You can nearly vote")
            chkflg = False
        else:
            print("You suck")
            chkflg = False
if __name__ == "__main__":
    main()