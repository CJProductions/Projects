#number guessing game
import random

def main():
    exits = False

    while exits == False:
        go = input("Do you want to play a game? Yes or No: ")
        if go == "yes":
            nums = random.randint(1, 100)
            guess = -1
            while guess != nums:
                guess = int(input("Guess a number between 1 and 100: "))
                if guess < nums:
                    outy = "Wrong, You are too low"
                elif guess > nums:
                    outy= "Wrong, You are too high"
                print(outy)
            print("Well done, you got the right number")
        else:
            exits=True

if __name__ == '__main__':
    main()