import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def doMessage(event):
    slbl.set(txt.get())

lbl = tk.Label(root)
lbl.configure(background='white', foreground='green')
slbl = tk.StringVar()
lbl.configure(textvariable=slbl)
lbl.configure(font=('Cascadia Code PL', '14', 'bold'))
lbl.grid(row=0, column=0, sticky='w')

txt = tk.Entry(root)
# txt.grid(row=0, column=0, sticky='nsew')
# txt.grid(row=0, column=0, sticky='nw')
txt.configure(font=('Cascadia Code PL', '14', 'normal'))
txt.configure(background='black', foreground='yellow')
txt.configure(insertbackground='yellow', insertwidth=16)
txt.bind('<KeyRelease>',doMessage)
txt.grid(row=1, column=0, sticky='w')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.mainloop()
