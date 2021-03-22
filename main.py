#!/usr/bin/env python3
# sudo apt-get install python3-tk

from tkinter import Tk, Frame, Label, Entry, Button
from tkinter import BOTH, LEFT

class App(Frame):

    def __init__(self):
        super().__init__()

        self.columns = 2
        self.rows = 8
        self.itemsArr=[]
        self.itemsMap={}
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
        data = Label(self, text="Cls")
        data.grid(row=3, column=3)
        self.data = data
        # bck = Button(self, text="Back")
        # bck.grid(row=1, column=1)
        # lbl = Button(self)
        # lbl.grid(row=1, column=2)
        # clo = Button(self, text="Close")
        # clo.grid(row=1, column=3)
        # frame.pack()

        for x in range(0, self.rows):
            for y in range(0, self.columns):
                lbl = Label(self, bg='#fff', width=10, height=5, 
                    cursor='hand2')
                lblId= 'x' + str(x) + 'y' + str(y)
                lbl.pos_attr= 'x' + str(x) + 'y' + str(y)
                lbl.config(text = 'x:' + str(x) + ', y: ' + str(y)) 
                self.itemsMap[lblId] = lbl
                lbl.bind("<Enter>", func=lambda event, t=lblId: self.mouseover(event, t))
                lbl.bind("<Leave>", func=lambda event, t=lblId: self.mouseout(event, t))
                lbl.bind("<ButtonRelease-1>", func=lambda event, t=lblId: self.mouseup(event, t))
                lbl.bind("<Button-1>", func=lambda event, t=lblId: self.mousedown(event, t))
                lbl.bind("<B1-Motion>", func=lambda event, t=lblId: self.mousedrag(event, t))
                lbl.grid(row=y, column=x)


        self.pack()

    def mouseover(self, event, element):
        self.data.configure(text=element)
        self.itemsMap[element].configure(background='#d0e3fc')

    def mouseout(self, enter, element):
        self.data.configure(text="")
        self.itemsMap[element].configure(background='#fff')

    def mousedown(self, enter, element):
        self.data.configure(text="down")

    def mouseup(self, enter, element):
        self.data.configure(text="up")
        for i in self.itemsMap:
            print(i)
            self.itemsMap[i].configure(background='#fff')

    def mousedrag(self, event, element):
        txt="drag: x:" + str(event.x )+ ", y: " + str(event.y)
        self.data.configure(text= txt)

def main():

    root = Tk()
    # root.geometry("+300+300")
    app = App()
    root.mainloop()


if __name__ == '__main__':
    main()