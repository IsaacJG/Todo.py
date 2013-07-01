#!/usr/bin/env python

import CLI.Constants

class Parser: 
    def __init__(self, args):
        self.args = args

    def parse(self):
        args = {}
        args['action'] = self.args[0]

        if len(self.args) > 1:
            if args['action'] == Constants.ACTION_LIST:
                args['action_switch'] = self.args[1]
                
            elif args['action'] == Constants.ACTION_ADD:
                args['task_name'] = self.args[1]
                try:
                    args['due_date'] = self.args[self.args.index(Constants.FLAG_DUEDATE)+1]
                except Exception:
                    pass
                try:
                    args['catagory'] = self.args[self.args.index(Constants.FLAG_CATAGORY)+1]
                except Exception:
                    pass

            elif args['action'] == Constants.ACTION_REMOVE:
                args['task_name'] = self.args[1]

            elif args['action'] == Constants.ACTION_EDIT:
                args['task_name'] = self.args[1]
                try:
                    args['due_date'] = self.args[self.args.index(Constants.FLAG_DUEDATE)+1]
                except Exception:
                    pass
                try:
                    args['catagory'] = self.args[self.args.index(Constants.FLAG_CATAGORY)+1]
                except Exception:
                    pass
        
        return args
