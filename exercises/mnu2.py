import tkinter as tk

root = tk.Tk()
root.title('Menu Example')

def mnuOpen():
    pass

def mnuSave():
    pass

menu = tk.Menu(root)
fmenu = tk.Menu(menu, tearoff=0)        # file menu
fmenu.add_command(label='Open', command=mnuOpen)
fmenu.add_command(label='Save As...', command=mnuSave)

menu.add_cascade(menu=fmenu, label='File')

root.config(menu=menu)

root.mainloop()