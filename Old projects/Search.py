import random as rnd

def linearSearch(listToSearch, item):

    i = 0
    while i <= len(listToSearch):
        if listToSearch[i] == item:
            return i
        else:
            i += 1
    return -1

def main():
    listToSearch = []
    for i in range(0, 10000):
        listToSearch.append(rnd.randint(0, 101))
    print(listToSearch)
    item = int(input("What would you like to search for?: "))
    result = linearSearch(listToSearch, item)
    if result == -1:
        print("The item you entered was not found.")
    else:
        print(f"the item is at position :{i}")

if __name__ == '__main__':
    main()