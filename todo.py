#!/usr/bin/env python

import os, sys

class Task:
    def __init__(self, task, due_date=None, catagory=None):
        self.task = task
        self.due_date = due_date
        self.catagory = catagory

    def __str__(self):
        return '{0}: {1} @ {2}'.format(self.catagory, self.task, self.due_date)

class TaskList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

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
