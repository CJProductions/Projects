def onlineCount(statuses):
    print(statuses.keys())
    print(statuses.values())
    check = len(statuses.values())
    print(check)

def main():
    statuses = {"Alice":"Online", "Bob":"Offline", "Eve":"Online"}
    option = int(input("press 1 otherwise this breaks"))
    match option:
        case 1:

                onlineCount(statuses)
if __name__ == '__main__':
    main()