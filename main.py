#!/usr/bin/env python3
# sudo apt-get install python3-tk

from tkinter import Tk, Frame, Label, Entry, Button, PhotoImage
from tkinter import BOTH, LEFT
import math

class App(Frame):

    def __init__(self):
        super().__init__()

        self.columns = 2
        self.rows = 8
        self.itemsArr=[]
        self.itemsMap={}
        self.isMouseDragging=False
        self.firstSelection=""
        self.lastSelection=""
        self.initUI()


    def initUI(self):

        self.master.title("Cursors")
        self.pack(fill=BOTH)

        for x in range(0, 100):
            self.rowconfigure(x, pad=5)
        for y in range(0, 100):
            self.columnconfigure(y, pad=5)

        info = Label(self, text="Cls")
        info.grid(row=0, column=0, columnspan=5)
        self.info = info

        for x in range(0, self.rows):
            for y in range(0, self.columns):
                # img = PhotoImage(width=1, height=1)
                lbl = Frame(self, bg='#fff', width=95, height=95, 
                    cursor='hand2')
                lblId= 'x' + str(x) + 'y' + str(y)
                lbl.pos_attr= 'x' + str(x) + 'y' + str(y)
                lbl.row_attr=x
                lbl.col_attr=y
                lbl.posX=x*100
                lbl.posY=y*100
                # lbl.config(text = 'x:' + str(x) + ', y: ' + str(y)) 
                self.itemsMap[lblId] = lbl
                lbl.bind("<Enter>", func=lambda event, t=lblId: self.mouseover(event, t))
                lbl.bind("<Leave>", func=lambda event, t=lblId: self.mouseout(event, t))
                lbl.bind("<ButtonRelease-1>", func=lambda event, t=lblId: self.mouseup(event, t))
                lbl.bind("<Button-1>", func=lambda event, t=lblId: self.mousedown(event, t))
                lbl.bind("<B1-Motion>", func=lambda event, t=lblId: self.mousedrag(event, t))
                lbl.grid(row=y+1, column=x)


        self.pack()

    def mouseover(self, event, element):
        self.info.configure(text=element)
        self.itemsMap[element].configure(background='#d0e3fc')

    def mouseout(self, enter, element):
        self.info.configure(text="")
        self.itemsMap[element].configure(background='#fff')

    def mousedown(self, enter, element):
        self.info.configure(text="down")
        self.firstSelection=element
        

    def mouseup(self, enter, element):
        self.info.configure(text="up")
        for i in self.itemsMap:
            self.itemsMap[i].configure(background='#fff')
        self.isMouseDragging=False

    def mousedrag(self, event, element):
        txt="drag: x:" + str(event.x )+ ", y: " + str(event.y)
        self.info.configure(text= txt)
        self.isMouseDragging=True
        self.itemsMap[element].configure(background='#d0e3fc')
        row=self.itemsMap[element].row_attr
        col=self.itemsMap[element].col_attr
        posX=self.itemsMap[element].posX
        posY=self.itemsMap[element].posY
        row_offset=math.floor((posX+event.x)/100)
        col_offset=math.floor((posY+event.y)/100)
        if row_offset < 0:
            row_offset = 0
           
        if col_offset < 0:
            col_offset = 0
        txt="drag: x:" + str(event.x )+ ", y: " + str(event.y) + ",row_offset:" + str(row_offset) + " ,col_offset:" + str(col_offset)
        self.info.configure(text= txt)

           
        for i in self.itemsMap:
            self.itemsMap[i].configure(background='#fff')
        for i in self.itemsMap:
            item = self.itemsMap[i]
            minX=min(row, row_offset)
            maxX=max(row, row_offset)
            minY=min(col, col_offset)
            maxY=max(col, col_offset)
            if item.row_attr >= minX and item.row_attr <= maxX and item.col_attr >= minY and item.col_attr <= maxY:
                item.configure(background='#d0e3fc')
               

def main():

    root = Tk()
    # root.geometry("+300+300")
    app = App()
    root.mainloop()


if __name__ == '__main__':
    main()