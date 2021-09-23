import tkinter as tk

root = tk.Tk()

lbl = tk.Label(root)
lbl.configure(text='This is a label')
# justify - when you have more than one line, they're justified.
# anchor - if you don't specify, the text will be centered.
lbl.configure(justify=tk.LEFT, anchor=tk.W)
lbl.configure(background='yellow', foreground='blue')
lbl.configure(font=('Cascadia Code PL', 14, 'normal'))
lbl.grid(row=0, column=0, sticky='nsew')

# this allows row=0/column=0 to expand as you stretch out the window.
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.mainloop()
