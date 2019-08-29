arrayOfTasks = []
userInput = ""
print("Congratulations! You're running R&J's Task List program.")


def addTask():
    newTask = input("Enter a new task to add to your list.")
    arrayOfTasks.append(newTask)


def listTask(array):
    if len(array) != 0:
        for x in array:
            print(x)
    else:
        print("Your task list is empty.")


def deleteTask(array):
    userIn = input("Which task to delete?")
    if userIn in array:
        array.remove(userIn)
    else:
        print("That task is not available.")


while userInput != 0:
    userInput = int(input(f'What would you like to do next?\n'
                          f'1. List all tasks.\n'
                          f'2. Add a task to the list.\n'
                          f'3. Delete a task.\n'
                          f'0. To quit the program'))
    if userInput == 1:
        listTask(arrayOfTasks)

    if userInput == 2:
        addTask()

    if userInput == 3:
        deleteTask(arrayOfTasks)
