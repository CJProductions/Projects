#treasure hunt game for list of lists
import random

def drawMap():
    # Tells the user that the treasure map is created and the map is printed
    print("Here is your treasure map")
    for r in tmap:
        # print out treasure map row by row
        print(r)
def hideTreasure():
    #creates empty list of coordinates
    coordinates = []
    #creates 10 coordinates
    for i in range(10):
        x = random.randint(0, 9)
        y = random.randint(0,9)
        #adds coordinates to list as list
        coordinates.append([x,y])
        #Takes the random coordinates back to main
        return coordinates

def main():
    tmap=[] #Creates an empty treasure map list
    # Gets random coordinates
    coordinates = hideTreasure()
    #Loops 10 times to create 10 rows of x's
    for i in range(10):
        row=["X","X","X","X","X","X","X","X","X","X"]
        #Adds list of xs to end of treasure map list
        tmap.append(row)



    print("Enter X coordinate of guess")
    xguess = int(input())
    print("Enter Y coordinate of guess")
    yguess = int(input())

    guess = [xguess, yguess]

    while guess != coordinates:
        if guess in coordinates:
            print("Treasure found")
        elif guess == [101, 101]:
            print(coordinates)
        else:
            print("Treasure not found")

if __name__ == "__main__":
    main()