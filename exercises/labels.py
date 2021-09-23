import tkinter as tk

root = tk.Tk()

lbl = tk.Label(root)
lbl.configure(text='This is a label')
lbl.pack(fill=tk.BOTH, expand=True)

root.mainloop()
