
import tkinter as tk
import sys

import dialogs

class FileMenu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        tk.Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.add_command(label="Open", command=self.cmdOpen)
        self.add_command(label="Close", command=self.cmdClose)
        self.add_command(label="Quit", command=self.cmdQuit)
    
    def cmdOpen(self):
        dialogs.OpenTreeDialog(self)
        pass

    def cmdClose(self):
        pass

    def cmdQuit(self):
        sys.exit()

class EditMenu(tk.Menu):
    pass

class DataMenu(tk.Menu):
    pass

class HelpMenu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        tk.Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.add_command(label="About", command=self.cmdAbout)
    
    def cmdAbout(self):
        dialogs.AboutDialog(self)

class MainMenu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        tk.Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.fileMenu = FileMenu(self, tearoff=0)
        self.add_cascade(label="File", menu=self.fileMenu)

        self.editMenu = EditMenu(self, tearoff=0)
        self.add_cascade(label="Edit", menu=self.editMenu)

        self.dataMenu = DataMenu(self, tearoff=0)
        self.add_cascade(label="Data", menu=self.dataMenu)

        self.helpMenu = HelpMenu(self, tearoff=0)
        self.add_cascade(label="Help", menu=self.helpMenu)