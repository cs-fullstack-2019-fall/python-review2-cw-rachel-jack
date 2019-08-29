theArray = ["wash clothes", "wash dishes"]
def listTask(array):
    for x in array:
        print(x)
listTask(theArray)
def deleteTask(array):
    userIn = input("which task to delete  ")
    array.remove(userIn)

