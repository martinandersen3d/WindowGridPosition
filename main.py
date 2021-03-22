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

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        entry = Entry(self)
        entry.grid(row=0, columnspan=4)
        cls = Button(self, text="Cls")
        cls.grid(row=1, column=0)
        bck = Button(self, text="Back")
        bck.grid(row=1, column=1)
        lbl = Button(self)
        lbl.grid(row=1, column=2)
        clo = Button(self, text="Close")
        clo.grid(row=1, column=3)
        # frame.pack()

        # for x in range(0, self.rows):
        #     for y in range(0, self.columns):
        #         lbl = Label(self, bg='SlateGray3', width=10, height=5, 
        #             cursor='tcross')
        #         lbl.grid(row=x, column=y)
        #         lbl.pack(side=LEFT, padx=3)
        #         # lbl.pack(row=x, column=y)
        #         self.items.append(lbl)
                
        
        # lbl1 = Label(frame, bg='SlateGray3', width=15, height=10,
        #     cursor='tcross')
        # lbl1.pack(side=LEFT, padx=3)

        # lbl2 = Label(frame, bg='SlateGray4', width=15, height=10,
        #     cursor='hand2')
        # lbl2.pack(side=LEFT)

        # lbl3 = Label(frame, bg='DarkSeaGreen3', width=15, height=10,
        #     cursor='heart')
        # lbl3.pack(side=LEFT, padx=3)

        # lbl4 = Label(frame, bg='DarkSeaGreen4', width=15, height=10,
        #     cursor='pencil')
        # lbl4.pack(side=LEFT)

        self.pack()

def main():

    root = Tk()
    # root.geometry("+300+300")
    app = App()
    root.mainloop()


if __name__ == '__main__':
    main()