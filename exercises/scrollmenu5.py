import tkinter as tk
from tkinter import scrolledtext
from tkinter import font

root = tk.Tk()

def menuCommand(choice):
    pass

# this is one way of changing tabs to spaces.
# def tabsToSpaces(event):
#     txt.insert(tk.INSERT, ' '*4)
#     return 'break'      # this stops the event from propagating further

menu = tk.Menu(root)
fmenu = tk.Menu(menu, tearoff=0)
fmenu.add_command(label='Open', command=lambda: menuCommand('O'))
menu.add_cascade(menu=fmenu, label='File')
root.config(menu=menu)

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

txt = scrolledtext.ScrolledText(frame)
txt.configure(background='black', foreground='white')
txt.configure(font=('Cascadia Code PL', 10, 'normal'))
txt.configure(insertbackground='yellow', insertwidth=4)
# txt.bind('<Tab>', tabsToSpaces)
# this is the other way of getting tabs to spaces
# but it does not work very well - don't know why.
fnt1 = font.Font(font=txt['font'])
tabw = fnt1.measure(' '*4)
tablist = tuple([tabw*x for x in range(1,10)])
txt.configure(tabs=tablist)
txt.pack(fill=tk.BOTH, expand=1)

txt.focus()

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.mainloop()