import random

def main():
    computerNumber = random.randint(1,10)
    print("Enter your guess")
    userGuess = int(input())
    
    if userGuess == computerNumber:
        print("Correct")
    else:
        print("Incorrect")

if __name__ == '__main__':
    main()

