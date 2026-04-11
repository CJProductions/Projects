def regionChecker(carInfo):
    region = ["A", "B", "C", "D", "E", "F", "G", "H", "K", "L", "M", "N", "O", "P", "R", "S", "V", "W", "Y"]
    area = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    reg = input("Please input your car's registration")

    for i in reg[0]:
        match i:
            case "A":
                print("Anglia")
            case "B":
                print("gurt")

def main():

    carInfo = []

    while True:
        try:
            print("Regional Registration checker")
            option = int(input("Please input your option\n"
                               "1.Region Checker\n"
                               "2.Exit"))
            match option:
                case 1:
                    regionChecker(carInfo)
                case 2:
                    exit()

        except ValueError:
            print("Invalid input")
if __name__ == '__main__':
    main()