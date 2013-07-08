#!/usr/bin/env python

import pickle
from os.path import exists as file_exists
from tkinter import simpledialog
from tkinter import *
from tkinter.messagebox import askquestion

class Task:
    def __init__(self, task, due_date=None, catagory='None'):
        self.task = task
        self.due_date = due_date
        self.catagory = catagory
        self.int_duedate = [due_date.split('/')[2], due_date.split('/')[0], due_date.split('/')[1]]
    
    def __str__(self):
        return '{0}: {1} @ {2}'.format(self.catagory, self.task, self.due_date)

    def __repr__(self):
        if self.due_date is not None and not self.due_date == '':
            return '[{0}] {1}'.format(self.due_date, self.task)
        else:
            return self.task

class TaskList:
    def load():
        if file_exists('todo.raw'):
            return pickle.load(open('todo.raw', 'rb'))

    def __init__(self):
        self.tasks = []
        self.visualizer = TaskListVisualizer(self)
        
    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def clear(self):
        self.tasks = []

    def get_task(self, name):
        for task in self.tasks:
            if task.task == name:
                return task
        
    def get_catagory(self, catagory):
        cat_list = []
        for task in self.tasks:
            if task.catagory == catagory:
                cat_list.append(task)
        return cat_list

    def get_catagories(self):
        cat_list = []
        for task in self.tasks:
            if cat_list.count(task.catagory) == 0:
                cat_list.append(task.catagory)
        return cat_list

    def save(self):
        with open('todo.txt', 'w') as todo_file:
            todo_file.write(str(self))
        pickle.dump(self, open('todo.raw', 'wb'))

    def __len__(self):
        return len(self.tasks)

    def __str__(self):
        return self.visualizer.by_catagory()

class TaskListVisualizer:
    def __init__(self, task_list):
        self.task_list = task_list

    def by_catagory(self):
        rtrn_str = ''
        catagories = sorted(self.task_list.get_catagories())
        for catagory in catagories:
            rtrn_str += '({0})\n'.format(catagory)
            tasks = sorted(self.task_list.get_catagory(catagory), key=lambda task: task.task)
            for task in tasks:
                rtrn_str += '    {0}\n'.format(repr(task))
        return rtrn_str

    def by_date(self):
        rtrn_str = ''
        tasks = sorted(self.task_list.tasks, key=lambda task: task.int_duedate, reverse=True)
        for task in tasks:
            rtrn_str += '{0}\n'.format(str(task))
        return rtrn_str

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
        try:
            name = add_task_dialog.name
            due_date = add_task_dialog.due_date if add_task_dialog.due_date != '' else None
            catagory = add_task_dialog.catagory if add_task_dialog.catagory != '' else None
            self.task_list.add_task(Task(add_task_dialog.name, add_task_dialog.due_date, add_task_dialog.catagory))
            self.refresh()
        except AttributeError:
            pass

    def remove_task(self):
        for selection in self.list_box.curselection():
            affirmatory = askquestion('Are you sure you want to remove task?', 'Are you sure you want to remove {0}?'.format(self.task_index[int(selection)].task))
            if affirmatory == 'yes':
                self.task_list.remove_task(self.task_index[int(selection)])
        self.refresh()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    def save(self):
        self.task_list.save()

if __name__ == '__main__':
    tasks_list = TaskList.load()
    if tasks_list:
        gui(tasks_list)
    else:
        gui(TaskList())