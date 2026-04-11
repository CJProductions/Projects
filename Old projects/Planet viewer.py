def viewPlanet(planets):

    for i in range(0, len(planets)):
        print(f"Name: {planets[i][0]}")
        print(f"Diameter: {planets[i][1]}")
        print(f"Colour: {planets[i][2]}")
        print()

def addPlanet(planets):

    planet = []
    planet_name = input("Input the name of your planet")
    planet_diameter = float(input("Please input the diameter of the planet"))
    planet_colour = input("Please input the colour of the planet")

    for i in range(len(planets)):
        print(i)
        TempLetterOne = planets[i][0][0]
        TempLetterTwo = planet_name[0]
        print(TempLetterOne , TempLetterTwo)
        if TempLetterOne > TempLetterTwo:
            pass
        elif TempLetterOne < TempLetterTwo:
            planet.append(planet_name)
            planet.append(planet_diameter)
            planet.append(planet_colour)
            planets.insert(i, planet)
            return planets



def main():

    # List of planets
    planets = [["Mercury", 4879.4, "Grey"], ["Venus", 12104, "Yellow"], ["Earth", 12742, "Blue"], ["Mars", 6779, "Red"],["Jupiter", 139890, "Brown"], ["Saturn", 74897, "Yellow"], ["Uranus", 50724, "Blue"],["Neptune", 49244, "Blue"]]

    # Loops the code until the user exits the program
    while True:

        try:

            option = int(input("Please select an option\n"
                                "1.View planets\n"
                                "2.Add a planet\n"
                                "3.Exit program"))

            match option:
                case 1:
                    viewPlanet(planets)
                case 2:
                    planets = addPlanet(planets)
                case 3:
                    exit()
                case 4:
                    print(planets[0][0][0])
                    planet_name = input("Input the name of your planet")
                    print(planet_name[0])
                    if "M" < "S":
                        print("True dat")

        except ValueError:
            print("Invalid option")

if __name__ == '__main__':
    main()