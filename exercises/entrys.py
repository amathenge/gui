import tkinter as tk

root = tk.Tk()

txt = tk.Entry(root)
# this causes the text box to fill the window, and stretch when it stretches.
txt.pack(fill=tk.BOTH, expand=True)

root.mainloop()
