import tkinter as tk

root = tk.Tk()

txt = tk.Entry(root)
# txt.grid(row=0, column=0, sticky='nsew')
# txt.grid(row=0, column=0, sticky='nw')
txt.grid(row=0, column=0, sticky='w')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.mainloop()
