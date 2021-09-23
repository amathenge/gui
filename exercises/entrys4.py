import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def showMessage(event):
    messagebox.showinfo('Info', 'A button has been pressed')

txt = tk.Entry(root)
# txt.grid(row=0, column=0, sticky='nsew')
# txt.grid(row=0, column=0, sticky='nw')
txt.configure(font=('Cascadia Code PL', '14', 'normal'))
txt.configure(background='black', foreground='yellow')
txt.configure(insertbackground='yellow', insertwidth=16)
txt.bind('<KeyRelease>',showMessage)
txt.grid(row=0, column=0, sticky='w')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.mainloop()
