# Works but no fleshed out

def capitalIndexes():
    letterPos = []
    capital = input("Please enter a word with capitals")
    for i in range(len(capital)):
        if capital[i].isupper():
            letterPos.append(i)
    return letterPos


def main():
    print("Capital index checker")
    letterPos = capitalIndexes()
    print(letterPos)


if __name__ == '__main__':
    main()