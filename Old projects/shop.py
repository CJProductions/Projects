def calculateTotal(income, qty, item):

    income = income + qty * item
    return income

def main():

    income = 0
    items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}  # List of items being sold

    for item in items.keys():  # Goes through each item of the list of things being sold
        chkflg = True
        while chkflg:
            try:
                qty = int(input(f"How many {item}s have you sold? "))  # asks for how many items have been sold
            except ValueError:
                print("You suck")
            else:
                chkflg = False
                income = calculateTotal(income, qty, items[item])

    print(f"\nThe income today was £{income:0.2f}")

if __name__ == "__main__":
    main()