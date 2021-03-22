import tkinter as tk
from tkinter import *
root = tk.Tk()
root.configure(background='black')
label_1=Label (root, width="20", height="3",bg="#EEE",relief="flat")
label_2=Label (root, width="20",height="3",bg="green")
label_3=Label (root, width="20", height="3",bg="blue")
label_4=Label (root, width="20", height="3",bg="white")
label_5=Label (root, width="20", height="3",bg="black")
label_6=Label (root, width="20", height="3",bg="grey")

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=0, column=2)
label_4.grid(row=1, column=0)
label_5.grid(row=1, column=1)
label_6.grid(row=1, column=2)

 

root.mainloop ()
