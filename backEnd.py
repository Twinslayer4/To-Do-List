import datetime
#Learn to save the to do list per instances
#Learn to give this program a UI
#Learn how to send this program as an app to my phone and set alerts. Look into Pyto 

class TaskManager:

    def __init__(self):
        self.taskLists = []
        self.dueDateList = []

    def addTask(self, task, dueDateString=""):
        dueDate = "N/A"

        if dueDateString.strip() != "":
            dueDate = datetime.datetime.strptime(dueDateString, "%Y-%m-%d")
        
        self.taskLists.append(task)
        self.dueDateList.append(dueDate)

    def delete(self, task):
        #Checks if task to be deleted is in the list before deleting
        if task in self.taskLists:
            index = self.taskLists.index(task)
            self.taskLists.pop(index)
            self.dueDateList.pop(index)

    def showTasks(self):
        #Returns if no items are in the task list.
        if  not self.taskLists:
            print("No tasks")
            return

        for tasks, dueDate in zip(self.taskLists, self.dueDateList):
            print(f"{tasks}, Due: {dueDate}")
    
    def saveFile(self):
        pass