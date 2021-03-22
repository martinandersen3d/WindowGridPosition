import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
style = ttk.Style()
style.theme_use("classic")
root.configure(background='black')

style.map("C.TButton",
   foreground=[('!active', 'black'),('pressed', 'red'), ('active', 'white')],
    background=[ ('!active','grey75'),('pressed', 'green'), ('active', 'black')]
    )
btr = ttk.Button(root, text="TEST BUTTON", style="C.TButton")
btr.grid(column=0,row=0,sticky='nsew');
root.mainloop()