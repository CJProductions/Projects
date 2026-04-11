def main():
    total = 0
    for i in range(6):
        num = int(input("Enter a number: "))
        total = total + num
        print(total)
    total = total // 6
    print(total)
if __name__ == '__main__':
    main()