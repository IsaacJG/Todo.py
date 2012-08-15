from Tkinter import *
from core import TaskList

'''def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=E)

Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()'''

class gui:
    def __init__(self, TaskList):
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
        
        list_box = Listbox(self.main_frame, width=100)
        list_box.grid(column=0, row=0, rowspan=2, sticky=(N, W, S))

        Button(self.main_frame, text='Add Task', command=self.add_task).grid(column=1, row=0, sticky=(N, E))
        Button(self.main_frame, text='Remove Task', command=self.remove_task).grid(column=1, row=1, sticky=(S, E))

        self.main_frame.columnconfigure(0, weight=3)
        self.main_frame.columnconfigure(1, weight=1)

        self.root.mainloop()

    def add_task(self):
        pass

    def remove_task(self):
        pass
        
if __name__ == '__main__':
    gui()
