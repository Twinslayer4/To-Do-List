

def main():
    commandNumber = 0
    taskLists = [];
    while commandNumber != 4:
        try:
            commandNumber = int(input("Enter 1 to input new task.\nEnter 2 to print out tasks.\nEnter 3 to delete a task.\nEnter 4 to end program.\n"))
        except:
            print("Invalid Output");
            continue
        if commandNumber == 1: # Input new tasks
            taskLists.append(input("Enter new task: "));
        elif commandNumber == 2:
            for i in range(len(taskLists)):
                print(f"{i+1}: {taskLists[i]}")
        elif commandNumber == 3: #Delete a task
            taskToDelete = int(input("Enter the number of the task to be deleted.")) -1
            taskLists.pop(taskToDelete)
        elif commandNumber == 4: #Quit program
            return;
        else: 
            print("Not a valid command")


main()