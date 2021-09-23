import tkinter as tk

root = tk.Tk()
root.title('Menu Example')

def mnuOpen():
    pass

menu = tk.Menu(root)
fmenu = tk.Menu(menu, tearoff=0)        # file menu
fmenu.add_command(label='Open', command=mnuOpen)
menu.add_cascade(menu=fmenu, label='File')

root.config(menu=menu)

root.mainloop()