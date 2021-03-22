#!/usr/bin/env python3
# sudo apt-get install python3-tk

from tkinter import Tk, Frame, Label, Entry, Button
from tkinter import BOTH, LEFT

class App(Frame):

    def __init__(self):
        super().__init__()

        self.columns = 2
        self.rows = 8
        self.items=[]
        self.initUI()


    def initUI(self):

        self.master.title("Cursors")
        self.pack(fill=BOTH)

        # frame = Frame(self, borderwidth=10)
        # frame.grid_rowconfigure(0, weight = 1) # rows will split space
        # frame.grid_rowconfigure(1, weight = 1) # rows will split space
        
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.columnconfigure(4, pad=3)
        self.columnconfigure(5, pad=3)
        self.columnconfigure(6, pad=3)
        self.columnconfigure(7, pad=3)
        self.columnconfigure(8, pad=3)
        self.columnconfigure(9, pad=3)
        self.columnconfigure(10, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)
        self.rowconfigure(8, pad=3)
        self.rowconfigure(9, pad=3)
        self.rowconfigure(10, pad=3)
        # entry = Entry(self)
        # entry.grid(row=0, columnspan=4)
        cls = Label(self, text="Cls")
        cls.grid(row=1, column=0)
        # bck = Button(self, text="Back")
        # bck.grid(row=1, column=1)
        # lbl = Button(self)
        # lbl.grid(row=1, column=2)
        # clo = Button(self, text="Close")
        # clo.grid(row=1, column=3)
        # frame.pack()

        for x in range(0, self.rows):
            for y in range(0, self.columns):
                lbl = Label(self, bg='SlateGray3', width=10, height=5, 
                    cursor='tcross')
                lbl.grid(row=y, column=x)

        self.pack()

def main():

    root = Tk()
    # root.geometry("+300+300")
    app = App()
    root.mainloop()


if __name__ == '__main__':
    main()