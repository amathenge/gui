import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('btn example')
frame = tk.Frame(root)
frame.pack(fill=None, expand=True)
# frame.pack(fill=tk.BOTH, expand=1)

def doInfo():
    messagebox.showinfo(title='Information', message='This is information')

def doWarn():
    messagebox.showwarning(title='Warning', message='This is a warning')

def doErr():
    messagebox.showerror(title='Error', message='This is an error')


button = tk.Button(frame)
button.configure(text=' SHOW INFORMATION ')
button.configure(command=doInfo)
button.grid(row=0, column=0, padx=5, pady=5)

button2 = tk.Button(frame)
button2.configure(text=' WARN MESSAGE ')
button2.configure(command=doWarn)
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = tk.Button(frame)
button3.configure(text=' ERROR MESSAGE ')
button3.configure(command=doErr)
button3.grid(row=0, column=2, padx=5, pady=5)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
