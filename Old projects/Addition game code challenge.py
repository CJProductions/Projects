#Imported random as we need random numbers to be put into the questions
import random

def main():
    #Sets the user score to 0 by default
    userScore = 0

    #Main menu option that I put here for slightly more robustness
    print("Addition game")
    startGame = int(input("Press 1 to start game"))
    if startGame == 1:
        #Loops the questions 5 times before the game is over
        for i in range(5):
            #Generates two random numbers to be added
            firstNum = random.randint(1, 50)
            secondNum = random.randint(1, 50)

            #Asks the user an addition question
            print("What is ", firstNum, "+", secondNum, "?")
            #Calculates the correct answer to compare with the user's answer
            answer = firstNum + secondNum
            #Asks the user for their input
            useranswer = int(input("Input your answer"))
            #Compares the user's input to the answer generated
            if useranswer == answer:
                print("Correct")
                #Adds one score if they're correct to the user's final tally
                userScore += 1
            else:
                print("Incorrect")
    #Tells the user their final score once the 5 questions has ended
    print("Game Over your score was ", userScore)









if __name__ == '__main__':
    main()
