#!/usr/bin/env python

from operator import attrgetter

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

    def length(self):
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
        # almost works...
        class TaskComp(object):
            def __init__(self, obj, *args):
                self.obj = obj
            def __comp(self, other):
                if other.__class__ == 'core.TaskComp':
                    if self.obj.due_date.count('/') == 0 or other.obj.due_date.count('/') == 0:
                        return -1

                    due = self.obj.due_date.split('/')
                    odue = other.obj.due_date.split('/')
                    if due[2] == odue[2]:
                        if due[1] < odue[1]:
                            return self.obj
                        elif due[1] > odue[1]:
                            return other.obj
                        else:
                            if due[0] < odue[0]:
                                return self.obj
                            elif due[0] > odue[0]:
                                return other.obj
                            else:
                                return None
                    elif due[2] < odue[2]:
                        return self.obj
                    else:
                        return other.obj
                else:
                    return None
                
            def __lt__(self, other):
                return True if self.__comp(other) == self.obj else False
            def __gt__(self, other):
                return True if self.__comp(other) == other.obj else False
            def __eq__(self, other):
                return True if self.__comp(other) == None else False
            def __le__(self, other):
                return True if self.__lt__(other) or self.__eq__(other) else False
            def __ge__(self, other):
                return True if self.__gt__(other) or self.__eq__(other) else False
            def __ne__(self, other):
                return True if self.__comp(other) == -1 else False
            
        rtrn_str = ''
        tasks = sorted(self.task_list.tasks, key=TaskComp)
        for task in tasks:
            rtrn_str += '{0}\n'.format(str(task))
        return rtrn_str
