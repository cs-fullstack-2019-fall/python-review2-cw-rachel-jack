arrayOfTasks = []
userInput = ""

def addTask():
    newTask = input("Enter a new task to add to your list.")
    arrayOfTasks.append(newTask)

while userInput != 0 :
    userInput = int(input(f'What would you like to do next?'
                      f'1. List all tasks.'
                      f'2. Add a task to the list.'
                      f'3. Delete a task.'
                      f'0. To quit the program'))
    if userInput == 2:
        addTask()

print (arrayOfTasks[0])



