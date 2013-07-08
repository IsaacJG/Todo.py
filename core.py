#!/usr/bin/env python

import pickle
from os.path import exists as file_exists

def save_tasks(task_list):
    with open('todo.txt', 'w') as todo_file:
        todo_file.write(str(task_list))
    pickle.dump(task_list, open('todo.raw', 'wb'))

def load_tasks():
    if file_exists('todo.raw'):
        task_list = pickle.load(open('todo.raw', 'rb'))
        return task_list

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

    def __len__(self):
        return self.tasks.length

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
