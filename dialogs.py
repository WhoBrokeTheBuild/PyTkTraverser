import tkinter as tk

import events

class AboutDialog(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.title("About PyTkTraverser")

        self.frame = tk.Frame(self, width=250, height=100)
        self.frame.pack(fill=None, expand=None)

        self.text = tk.Label(self.frame, text=
            "PyTkTraverser v0.0.1\n\n"
            "© 2019 Stephen Lane-Walsh\n"
            "MIT License"
        )
        self.text.place(relx=0.5, rely=0.5, anchor='center')

        self.wait_window()

class OpenTreeDialog(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.title("Open Tree")

        self.frame = tk.Frame(self)
        self.frame.pack(fill=None, expand=None, padx=10, pady=20)

        self.inputFrame = tk.Frame(self.frame)
        self.inputFrame.pack(fill=None, expand=None)

        self.treeLabel = tk.Label(self.inputFrame, text="Tree:")
        self.treeLabel.grid(row=0, column=0, padx=(0, 10), pady=(0, 10))

        self.treeInput = tk.Entry(self.inputFrame, width=12)
        self.treeInput.grid(row=0, column=1, sticky="w", pady=(0, 10))
        self.treeInput.bind("<Control-a>", events.selectAllHandler)

        self.shotLabel = tk.Label(self.inputFrame, text="Shot:")
        self.shotLabel.grid(row=1, column=0, padx=(0, 10), pady=(0, 10))

        self.shotInput = tk.Entry(self.inputFrame, width=10, validate='all', validatecommand=(self.register(self.validateShotInput),"%P"))
        self.shotInput.grid(row=1, column=1, sticky="w", pady=(0, 10))
        self.shotInput.bind("<Control-a>", events.selectAllHandler)

        self.modes = {
            1: 'NORMAL',
            2: 'READONLY',
            3: 'EDIT',
            4: 'NEW',
        }
        self.mode = tk.IntVar()

        self.modeReadWrite = tk.Radiobutton(self.frame, text="Read/Write", variable=self.mode, value=1)
        self.modeReadWrite.pack(anchor="w")
        self.modeReadWrite.select()

        self.modeReadOnly = tk.Radiobutton(self.frame, text="Read Only", variable=self.mode, value=2)
        self.modeReadOnly.pack(anchor="w")
        self.modeReadOnly.deselect()

        self.modeEdit = tk.Radiobutton(self.frame, text="Edit", variable=self.mode, value=3)
        self.modeEdit.pack(anchor="w")
        self.modeEdit.deselect()

        self.modeNew = tk.Radiobutton(self.frame, text="New", variable=self.mode, value=4)
        self.modeNew.pack(anchor="w")
        self.modeNew.deselect()

        tk.Frame(self.frame, height=2, relief="raised", borderwidth=1).pack(fill="both", expand=True, pady=10)

        self.openButton = tk.Button(self.frame, text="Open", command=self.commandOpen)
        self.openButton.pack(side="right")
        self.cancelButton = tk.Button(self.frame, text="Cancel", command=self.commandCancel)
        self.cancelButton.pack(side="right")

        self.wait_window()

    def validateShotInput(self, P):
        if P == "" or P == "-":
            return True
        try:
            int(P)
            return True
        except ValueError:
            return False
        

    def commandOpen(self):
        print("tree={}, mode={}, shot={}".format(self.treeInput.get(), self.modes[self.mode.get()], self.shotInput.get()))
        self.destroy()

    def commandCancel(self):
        self.destroy()