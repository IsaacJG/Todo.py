#!/usr/bin/env python

import os, sys

class Task:
    def __init__(self, task, due_date=None, catagory=None):
        self.task = task
        self.due_date = due_date
        self.catagory = catagory

    def __str__(self):
        return '{0}: {1} @ {2}'.format(self.catagory, self.task, self.due_date)

    def __repr__(self):
        if self.due_date is not None:
            return '[{0}] {1}'.format(self.due_date, self.task)
        else:
            return self.task

class TaskList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_task(self, name):
        for task in self.tasks:
            if task.name == name:
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

    def length(self):
        return self.tasks.length

    def __str__(self):
        s = ''
        for task in self.tasks:
            s += task.__str__() + '\n'
        return s

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

#Uncomment this to test:
'''if __name__ == '__main__':
    todo = TaskList()
    todo.add_task(Task('get flashdrive back', None, 'etc'))
    todo.add_task(Task('3 ring binder for calculus', '8/13/12', 'school'))
    todo.add_task(Task('Finish calculus packet', '8/13/12', 'school'))
    todo.add_task(Task('Finish new todo manager', None, 'etc'))
    todo.add_task(Task('Finish IJGSecBuild1', '8/15/12', 'school'))
    todoVisualizer = TaskListVisualizer(todo)
    print(todoVisualizer.by_catagory())'''
