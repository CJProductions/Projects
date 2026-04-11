def viewlist(todo):
    if len(todo)>0:
        print("Here are all the tasks you have with their due date")
        print("")
        for i in range(len(todo)):
            print(i, ". ", todo[i][0],todo[i][2])
            print("")
    else:
        print("No tasks in list, add some first")
        print("")


def viewtask(todo):
    if len(todo)>0:
        print("choose a task, by number, to view its full details")
        print("")
        viewlist(todo)
        print("Enter the number of the task you wish to view")
        print("")

        while True:
            opt = int(input("Enter the number"))
            print("")
            if opt>len(todo):
                print("That task number doesnt exist, try again")
                print("")
            else:
                print("Here is your task:")
                print("Task: ", opt, " ",todo[opt-1][0],todo[opt-1][1],todo[opt-1][2],todo[opt-1][3])
                print("")
                break
    else:
        print("You do not have any tasks to view")
        print("")

def addtask():
    while True:
        brief = input("Enter the short name for the task, only put 20 characters max")
        print("")
        #Checks the input to see if it is less than characters and will get the user to retry if it is too long
        if len(brief) > 20:
            print("That was too long, 20 chars only please")
            print("")
        elif len(brief) >= 2:
            print("Brief version noted")
            print("")
            break
        elif len(brief) < 2:
            print("Task name is too short please try a longer name")
            print("")

    long = input("Enter a longer description of the task")
    print("")
    day = input("Enter a day of the month, in digits, the task is due")
    print("")
    month = input("Enter a month, in digits, the task is due")
    print("")
    year = input("Enter a year, in digits, the task is due")

    datey = day+"/"+month+"/"+year
    task = [brief, long, datey, "n"] #brief descript, long details, date its due and if its completed or not y or n
    return task

def removetask(todo): # Removes a task from the list
    if len(todo)>0: # Asks the user which task they would like to remove and displays the task list
        print("Choose a task to remove from the to list")
        print("")
        print("available tasks:")
        print("")
        viewlist(todo)
        print("Enter the number of the task you wish to remove")
        print("")

        #Asks the user to input a number to select the task they want to delete
        while True:
            opt = int(input("Enter the number"))
            #If they number they input is greater than the amount of tasks displayed it will retry the input
            if opt > len(todo):
                print("That task number doesnt exist, try again")
                print("")
            #Otherwise if the user selects a valid option it will delete the selected option by indexing the corresponding number to the option chosen
            else:
                todo.pop(opt)
                print("Your task has been removed")
                print("")
                return todo #Returns the new to do list with the deleted changes
    else:
        print("You do not have any tasks to view")


def main():
    todo = [] #main list of tasks, list of lists to be used.
    opt=0

    #If the user doesn't press 7 then the program won't end
    while opt!=7:
        print("")
        print("Welcome to the ToDo list App")
        print("")
        print("1. View the Todo list")
        print("2. View the details of a specific task")
        print("3. Add a new task")
        print("4. Delete a task")
        print("")
        print('7. Exit')
        print("")


         #Asks the user to input an option that will then run the subroutines based on the option picked
        opt = int(input("Enter the number of the option you wish to use"))

        if opt==1:
            viewlist(todo)
        elif opt==2:
            viewtask(todo)
        elif opt==3:
            todo.append(addtask())
        elif opt==4:
            todo=removetask(todo)
            # Extra room between numbers to add other functions
        elif opt==7:
            print("Thank you for using The ToDo List App, see ya!")



if __name__ == '__main__':
    main()