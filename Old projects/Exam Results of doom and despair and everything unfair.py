def removeStudent(students):
    print("What is the position you want to remove")
    print(students)
    pos = int(input())
    students.pop(pos)

    return students
def addStudent(students):
    print("What is the student's name?")
    name = input()
    print("What is the student's grade?")
    grade = input()
    students.append([name, grade])
    return students

def displayStudents(students):
    for i in range(0,len(students)):
        print("Name:",students[i][0])
        print("Grade:",students[i][1])

def main():
    students = [["Bob", 9], ["Lucy", 6], ["Max", 4], ["Jo", 8], ["Terry", 3]]
    studentNames = ["Bob","Lucy","Max","Jo","Terry"]
    studentGrades = [9,6,4,8,3]
    print("1. Display students and grades")
    print("2. Add a student and grade")
    print("3. Remove a student and grade")
    print("4.Exit")
    print("What would you like to do?")
    choice = int(input())
    while choice != 4:
        if choice == 1:
            displayStudents(students)
        elif choice == 2:
            students = addStudent(students)
        elif choice == 3:
            students = removeStudent(students)

        print("What would you like to do?")
        choice = int(input())


if __name__ == "__main__":
    main()