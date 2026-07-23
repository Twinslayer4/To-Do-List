import tkinter as tk
from tkinter import *
from tkinter import ttk
from backEnd import TaskManager

class TaskManagerDesktopApp:
    def __init__(self, root):
        self.manager = TaskManager()