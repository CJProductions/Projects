def main():
    HOURLYRATE = 32.50
    PAINTCHARGE = 1
    ROUGHPAINT = 1.5
    exit = False

    print("Room Paint Job Calculator")
    while exit == False:

        option = input("Enter the size of the room or type exit to quit")
        if option == "small":
            paint = input("Are you using rough or regular paint")
            if paint == "rough":
                print(HOURLYRATE * ROUGHPAINT * 6)
            elif paint == "regular":
                print(HOURLYRATE * PAINTCHARGE * 6)

        elif option == "medium":
            print("spongebob")
        elif option == "large":
            print("I'm spongebob")
        elif option == "exit" or "quit":
            exit = True
        else:
            print("Invalid option please enter a valid choice")

if __name__ == "__main__":
    main()