import tkinter as tk

root = tk.Tk()
root.title('Menu Example')

def mnuOpen():
    pass

def mnuSave():
    pass

def mnuClose():
    pass

menu = tk.Menu(root)
fmenu = tk.Menu(menu, tearoff=0)        # file menu
fmenu.add_command(label='Open', command=mnuOpen)
fmenu.add_command(label='Save As...', command=mnuSave)
fmenu.add_separator()
fmenu.add_command(label='Close', command=mnuClose)

menu.add_cascade(menu=fmenu, label='File')

root.config(menu=menu)

root.mainloop()