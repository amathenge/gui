import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('btn example')
frame = tk.Frame(root)
frame.pack(fill=None, expand=True)
# frame.pack(fill=tk.BOTH, expand=1)

def doMessage():
    messagebox.showinfo(title='Information', message='button pressed')

button = tk.Button(frame)
button.configure(text=' SHOW DIALOG ')
button.configure(command=doMessage)
button.grid(row=0, column=0, padx=5, pady=5)
# button.grid_rowconfigure(0, weight=1)
# button.grid_columnconfigure(0, weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
