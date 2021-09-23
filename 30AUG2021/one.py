#!/usr/bin/env python
#
# Exercises on using Tcl/Tk
#
from tkinter import *
from tkinter import ttk

root = Tk()
# labels.

lbl1 = ttk.Label(root, text='Label 1:')
lbl1.configure(font = ('Cascadia Code PL', 11, 'normal'))
lbl1.configure(foreground = 'blue')
lbl1.configure(background = 'grey')
lbl1.configure(width=10)
lbl1.configure(anchor='e')
lbl1.grid(row=0, column=0, pady=2, padx=5)

lbl2 = ttk.Label(root, text='Label 2:')
lbl2.configure(font = ('Cascadia Code PL', 11, 'normal'))
lbl2.configure(foreground = 'white')
lbl2.configure(background = 'black')
lbl2.configure(width=10)
lbl2.configure(anchor='e')
lbl2.grid(row=1, column=0, pady=2, padx=5)

lbl3 = ttk.Label(root, text='Label 3:')
lbl3.configure(font = ('Cascadia Code PL', 11, 'normal'))
lbl3.configure(foreground = 'red')
lbl3.configure(background = 'yellow')
lbl3.configure(width=10)
lbl3.configure(anchor='e')
lbl3.grid(row=3, column=0, pady=2, padx=5)

lbl4 = ttk.Label(root, text='Label 4:')
lbl4.configure(font = ('Cascadia Code PL', 11, 'normal'))
lbl4.configure(foreground = 'yellow')
lbl4.configure(background = 'blue')
lbl4.configure(width=10)
lbl4.configure(anchor='e')
lbl4.grid(row=4, column=0, pady=2, padx=5)

# Text boxes

# uisng TTK Entry boxes, you have to set the colours using styles.
style = ttk.Style(root)
style.theme_use('clam')
style.configure('T1.TEntry', foreground='blue', fieldbackground='yellow', background='yellow')
style.configure('T1.TEntry', insertcolor='blue', insertwidth='8')
txt1 = ttk.Entry(root, font = ('Cascadia Code PL', 11, 'normal'), style='T1.TEntry')
txt1.grid(row=0, column=1, padx=5)

style.configure('T2.TEntry', foreground='yellow', fieldbackground='black', background='black')
style.configure('T2.TEntry', insertcolor='yellow', insertwidth='8')
txt2 = ttk.Entry(root, font=('Cascadia Code PL', 11, 'normal'), style='T2.TEntry')
txt2.grid(row=1, column=1, padx=5)

'''
txt4 = ttk.Entry(root, width=35, background='blue', foreground='yellow')
txt4.configure(style='T1.Entry')
txt4.grid(row=2,column=1,pady=2,padx=5)
'''

root.mainloop()
