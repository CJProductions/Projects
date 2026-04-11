def main():
    print("Car Park Charges")

    #Asks for the numberplate
    print("Enter numberplate")
    numPlate = input()
    print("Enter length of stay")
    hours = input()
    if hours >= 2:
        charge = time * 0.5
    else:
        charge = time * 2
    print("Charge is:", charge)

if __name__ == "__main__":
    main()