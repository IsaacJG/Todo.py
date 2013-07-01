#!/usr/bin/env python

import os
import pickle
import CLI.Constants as Constants
from core import TaskList
from core import Task
from CLI.ArgParser import Parser

def main(argv):
    task_list = pickle.load(open('todo.raw', 'r')) if os.path.exists('todo.raw') else TaskList()
    args = Parser(argv).parse()
    if args['action'] == Constants.ACTION_LIST:
        if args.has_key('action_switch'):
            if args['action_switch'] == Constants.FLAG_ORDERBYDATE:
                print(task_list.visualizer.by_date())
        else:
            print(task_list)

    elif args['action'] == Constants.ACTION_ADD:
        task_name = args['task_name']
        catagory = None
        due_date = None
        if args.has_key('catagory'):
            catagory = args['catagory']
        if args.has_key('due_date'):
            due_date = args['due_date']
        task_list.add_task(Task(task_name, due_date, catagory))

    elif args['action'] == Constants.ACTION_REMOVE:
        task_list.remove_task(task_list.get_task(args['task_name']))

    elif args['action'] == Constants.ACTION_EDIT:
        task = task_list.get_task(args['task_name'])
        if args.has_key('new_name'):
            task.task = args['new_name']
        if args.has_key('due_date'):
            task.due_date = args['due_date']
        if args.has_key('catagory'):
            task.catagory = args['catagory']

    elif args['action'] == Constants.ACTION_CLEAR:
        task_list.clear()
    else:
        print('''
Usage: python todo.py [action] [args]

Actions                 Args
------------------------------
add                 (required) name
                    -d due date
                    -cat catagory

remove              (required) name

edit                (required) name
                    -d due date
                    -cat catagory
                    -rn rename

clear               

list                -date
''')

    todo_txt = open('todo.txt', 'w')
    todo_txt.write(repr(task_list))
    pickle.dump(task_list, open('todo.raw', 'w'))
