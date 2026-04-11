from logging import exception

def addJob(jobList, HOURLYRATE, SMALL, MEDIUM, LARGE, TOUGHPAINT):
    list = []
    jobmatch = False
    paintmatch = False
    jobPay = 0
    hoursSpent = 0
    name = input("Please enter clients name: ")
    list.append(name)
    list.append(hoursSpent)
    while jobmatch == False:

        job = input("Please enter job length: ")
        if job == "small":
            list.append(SMALL)
            jobPay = (SMALL * HOURLYRATE)
            jobmatch = True
        elif job == "medium":
            list.append(MEDIUM)
            jobPay = (MEDIUM * HOURLYRATE)
            jobmatch = True
        elif job == "large":
            list.append(LARGE)
            jobPay = (LARGE * HOURLYRATE)
        else:
            print("Please enter a valid job length")

    while paintmatch == False:

        paint = input("Please enter paint type(tough or regular): ")
        if paint == "tough":
            jobPay *= TOUGHPAINT
            paintmatch = True
        elif paint == "regular":
            jobPay *= 1
            paintmatch = True
        else:
            print("Please enter a valid paint type")

        list.append(jobPay)
        jobList.append(list)
        print("Job added")

        return jobList


def viewJob(jobList):

    for i in jobList:
        print(i)

    if jobList == []:
        print("No jobs entered")

def editJob(jobList):

    if jobList == []:
        print("No jobs entered")

    for i in jobList:
        print("Select job", i)
    jobSelection = int(input("Please enter which job you want to edit(0-10)"))
    if jobSelection > len(jobList):
        print("Please enter a valid job number")
    else:
        editTime = int(input("Please enter how many hours you have worked: "))
        jobList[jobSelection][2] -= editTime
        jobList[jobSelection][1] += editTime
        print(jobList)

    return jobList

def removeJob(jobList):

    for i in jobList:
        print(i)
    jobSelection = int(input("Please enter which job you want to remove(0-10): "))
    if jobSelection > len(jobList):
        print("Please enter a valid job number")
    else:
        jobList.pop(jobSelection)
        print("Job removed")

    return jobList

def main():

    HOURLYRATE = 32.50
    SMALL = 6
    MEDIUM = 10
    LARGE = 20
    TOUGHPAINT = 1.5
    jobList = []

    while True:
        try:
            print("Decorator Quote Calculator \n"
                  "1.Add Job \n"
                  "2.View Job \n"
                  "3.Edit Job \n"
                  "4.Remove Job \n"
                  "5.Exit")
            option = float(input("Enter a number: "))
            match option:
                case 1:
                    addJob(jobList, HOURLYRATE, SMALL, MEDIUM, LARGE, TOUGHPAINT)
                case 2:
                    viewJob(jobList)
                case 3:
                    editJob(jobList)
                case 4:
                    removeJob(jobList)
                case 5:
                    exit()

        except ValueError:
            print("Invalid input")

if __name__ == '__main__':
    main()