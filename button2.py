import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()

style = ttk.Style(root)
#style.theme_use("clam")


style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

btr = ttk.Button(root, text="TEST BUTTON", style="C.TButton")
btr.pack()

root.mainloop()