import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()

def menuCommand(choice):
    if choice == 'O':
        fname = filedialog.askopenfilename(
            filetypes = (
                ('Python Source', '*.py'),
                ('HTML Source', '*.htm;*.html'),
                ('Text Files', '*.txt'),
                ('All Files', '*.*')
            )
        )
        if fname != '':
            f = open(fname, 'r')
            txt.delete('1.0', 'end')
            txt.insert('1.0', f.read())
            f.close()

# this is one way of changing tabs to spaces.
# THIS IS THE BEST METHOD, PROVIDES THE MOST CONSISTENT RESULTS.
# FROM THE EXAMPLES scrollmenu1..5
def tabsToSpaces(event):
    mr = int(txt.index(tk.INSERT).split('.')[0])
    mc = int(txt.index(tk.INSERT).split('.')[1])
    nextTab = 4-(mc%4)
    # if nextTab == 0:
    #     nextTab = 4
    txt.insert(tk.INSERT, ' '*nextTab)
    return 'break'      # this stops the event from propagating further

menu = tk.Menu(root)
fmenu = tk.Menu(menu, tearoff=0)
fmenu.add_command(label='Open', command=lambda: menuCommand('O'))
menu.add_cascade(menu=fmenu, label='File')
root.config(menu=menu)

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

txt = scrolledtext.ScrolledText(frame)
txt.configure(background='black', foreground='white')
txt.configure(font=('Cascadia Code PL', 10, 'normal'))
txt.configure(insertbackground='yellow', insertwidth=4)
txt.bind('<Tab>', tabsToSpaces)
txt.pack(fill=tk.BOTH, expand=1)

txt.focus()

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.mainloop()