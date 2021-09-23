import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title('Scroll 2')

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

txt = scrolledtext.ScrolledText(frame)
txt.configure(wrap=tk.WORD)
txt.pack(fill=tk.BOTH, expand=True)

root.mainloop()
