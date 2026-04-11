def startGame(countries):
    guess = input("Please enter a country in Africa")


def main():
    countries = ["Algeria”, “Angola”, “Benin”, “Botswana”, “BurkinaFaso”, “Burundi”, “CaboVerde”, “Cameroon”, “CentralAfricanRepublic”, “Chad”, “Comoros”, “IvoryCoast”, “Djibouti”, “DemocraticRepublicoftheCongo”, “Egypt”, “EquatorialGuinea”, “Eritrea”, “Eswatini”, “Ethiopia”, “Gabon”, “Gambia”, “Ghana”, “Guinea”, “Guinea - Bissau”, “Kenya”, “Lesotho”, “Liberia”, “Libya”, “Madagascar”, “Malawi”, “Mali”, “Mauritania”, “Mauritius”, “Morocco”, “Mozambique”, “Namibia”, “Niger”, “Nigeria”, “RepublicoftheCongo”, “Rwanda”, “SaoTome & Principe”, “Senegal”, “Seychelles”, “SierraLeone”, “Somalia”, “SouthAfrica”, “SouthSudan”, “Sudan”, “Tanzania”, “Togo”, “Tunisia”, “Uganda”, “Zambia”, “Zimbabwe"]
    chkflg = True
    while chkflg == True:
        try:

            option = int(input("Please choose an option\n"
                            "1.Start game\n"
                            "2.Exit\n"
                               ""))

            match option:
                case 1:
                    startGame(countries)
                case 2:
                    exit()

        except ValueError:
            print("Invalid option")

if __name__ == '__main__':
    main()