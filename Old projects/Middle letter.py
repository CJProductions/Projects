def mid():
    word = input("Input a word fr fr")
    lenword = len(word)%2
    if lenword == 0:
        print("")
    else:
        unEvenWord = len(word)//2
        print(word[unEvenWord])




def main():
    print("Middle Doohickey")
    mid()
if __name__ == '__main__':
    main()