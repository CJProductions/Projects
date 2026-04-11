globalName = "Bob"
globalAge = 67
def changeVotingAge():
    global globalAge
    globalAge = 69

def canVote(localAge):
    if localAge < globalAge:
        print("You can't vote")
    else:
        print("You can vote")
def main():
    print(int(round(12.89)))
    print("Enter name")
    localName = input()
    print(localName)
    print("Enter age")
    localAge = int(input())
    canVote(localAge)
    changeVotingAge()
    canVote(localAge)
if __name__ == "__main__":
    main()