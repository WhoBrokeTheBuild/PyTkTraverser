#!/usr/bin/python3

import tkinter as tk
import tkinter.ttk as ttk

import menus

class MainWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.mainMenu = menus.MainMenu(self)
        self.parent.config(menu=self.mainMenu)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("PyTkTraverser")
    MainWindow(root, width=300, height=500).pack(fill=None, expand=None)
    root.mainloop()
