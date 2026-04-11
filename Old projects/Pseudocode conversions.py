def main():
    startMiles = int(input("Enter a miles: "))
    endMiles = int(input("Enter a miles: "))
    averageSpeed = int(input("Enter average speed: "))
    if averageSpeed >= 60:
        riskRating = (endMiles - startMiles) * averageSpeed * 1.6
    else:
        riskRating = (endMiles - startMiles) * averageSpeed * 0.9
    print(riskRating)
if __name__ == '__main__':
    main()