import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()

txt = scrolledtext.ScrolledText(root)
txt.pack(fill=tk.BOTH, expand=True)

root.mainloop()
