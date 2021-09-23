import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title('Scroll 2')

txt = scrolledtext.ScrolledText(root)
txt.configure(wrap=tk.WORD)
txt.pack(fill=tk.BOTH, expand=True)

root.mainloop()
