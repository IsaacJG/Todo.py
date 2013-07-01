#!/usr/bin/python

import os
from tkinter import simpledialog
from tkinter import *
from tkinter.messagebox import askquestion
from core import Task
from core import TaskList
from pickle import load
from pickle import dump


#class AddTaskDialog(tkSimpleDialog.Dialog):
class AddTaskDialog(simpledialog.Dialog):
    def body(self, master):
        Label(master, text='Name:').grid(row=0)
        Label(master, text='Due date:').grid(row=1)
        Label(master, text='Catagory:').grid(row=2)

        self.e1 = Entry(master)
        self.e2 = Entry(master)
        self.e3 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        return self.e1

    def apply(self):
        self.name = self.e1.get()
        self.due_date = self.e2.get()
        self.catagory = self.e3.get()

    
class gui:
    def __init__(self, task_list):
        self.task_list = task_list
        self.task_index = []
        
        self.root = Tk()
        self.root.title('Todo.py')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.main_frame = Frame(self.root)

        
        self.main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.main_frame.columnconfigure(0, weight=3)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.rowconfigure(2, weight=10)
        
        self.list_box = Listbox(self.main_frame, width=75, height=20, selectmode=EXTENDED, activestyle='none')
        self.list_box.grid(column=0, row=0, rowspan=3, sticky=(N, W, S))
        self.refresh()

        Button(self.main_frame, text='Add Task', command=self.add_task, width=20).grid(column=1, row=0, padx=10, pady=5, sticky=(N, E))
        Button(self.main_frame, text='Remove Task', command=self.remove_task, width=20).grid(column=1, row=1, padx=10, sticky=(E))
        Button(self.main_frame, text='Save', command=self.save, width=20).grid(column=1, row=2, padx=10, pady=5, sticky=(S, E))

        self.main_frame.columnconfigure(0, weight=3)
        self.main_frame.columnconfigure(1, weight=1)

        self.root.mainloop()

    def refresh(self):
        self.task_index = []
        self.list_box.delete(0, self.list_box.size()+1)
        tasks = [task for task in self.task_list.tasks]
        for i in range(len(tasks)):
            self.list_box.insert(i, str(tasks[i]))
            self.task_index.append(tasks[i])

    def add_task(self):
        add_task_dialog = AddTaskDialog(self.root)
        name = add_task_dialog.name
        due_date = add_task_dialog.due_date if add_task_dialog.due_date != '' else None
        catagory = add_task_dialog.catagory if add_task_dialog.catagory != '' else None
        self.task_list.add_task(Task(add_task_dialog.name, add_task_dialog.due_date, add_task_dialog.catagory))
        self.refresh()

    def remove_task(self):
        for selection in self.list_box.curselection():
            affirmatory = askquestion('Are you sure you want to remove task?', 'Are you sure you want to remove {0}?'.format(self.task_index[int(selection)].task))
            if affirmatory == 'yes':
                self.task_list.remove_task(self.task_index[int(selection)])
        self.refresh()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    def save(self):
        with open('todo.txt', 'w') as todo_txt:
            todo_txt.write(str(self.task_list))
        dump(self.task_list, open('todo.raw', 'w'))
        
if __name__ == '__main__':
    if os.path.exists('todo.raw'):
        gui(load(open('todo.raw', 'r')))
    else:
        gui(TaskList())
