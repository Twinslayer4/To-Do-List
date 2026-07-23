import tkinter as tk
from tkinter import *
from tkinter import ttk
from backEnd import TaskManager

class TaskManagerDesktopApp:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title = "Desktop Task Manager"  
        # style = ttk.Style()
        # style.configure('labels',font_color)  
        mainFrame = ttk.Frame(root, 
                              padding=(10, 10, 20, 20), 
                              borderwidth=2, 
                              relief= SUNKEN)
        mainFrame.grid(column=0, row=0)
        #self.image = PhotoImage(file="images.png")

        label = ttk.Label(mainFrame, 
                          text= "Hello World", 
                          #image= self.image, 
                          compound=TOP)
        
        label.grid(column=1, row=1)

        taskText = StringVar()
        TextEntry = ttk.Entry(root, 
                              textvariable=taskText,
                              width= 25)
        TextEntry.grid(column= 1, row = 0)

        dateText = StringVar()
        dateEntry = ttk.Entry(root, 
                              textvariable=dateText,
                              width= 25, )
        dateEntry.grid(column=1, row=1)

        AddTaskButton = ttk.Button(root, text="Add Tasks", command=self.addTask())
        AddTaskButton.grid(column=0, row= 2)


    def addTask(self):
         pass
    def deleteTask(self):
         pass
    def refreshTask(self):
         pass
        
        
        

if __name__ == "__main__":
        root = tk.Tk()
        app = TaskManagerDesktopApp(root)
        root.mainloop()