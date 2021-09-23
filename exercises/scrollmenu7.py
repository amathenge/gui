import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()

def menuCommand(choice):
    if choice == 'N':
        answer = messagebox.askokcancel(title='Clear Contents', message='Clear Notepad?')
        if answer == True:
            txt.delete('1.0', 'end')

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

    if choice == 'S':
        fname = filedialog.asksaveasfilename(
            filetypes=(
                ('Python Source', '*.py'),
                ('HTML Source', '*.html;*.htm'),
                ('Text File', '*.txt'),
                ('All Files', '*.*')
            )
        )
        if fname != '':
            f = open(fname, 'w')
            f.write(txt.get('1.0', 'end'))
            f.close()

    if choice == 'E':
        answer = messagebox.askokcancel(title='Quit?', message='Quit Application?')
        if answer == True:
            root.destroy()

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
fmenu.add_command(label='New', command=lambda: menuCommand('N'))
fmenu.add_command(label='Open', command=lambda: menuCommand('O'))
fmenu.add_command(label='Save As...', command=lambda: menuCommand('S'))
menu.add_cascade(menu=fmenu, label='File')
menu.add_command(label='Quit', command=lambda: menuCommand('E'))

root.config(menu=menu)

bframe = tk.Frame(root)
bframe.pack(fill=tk.X, expand=1)

btn = tk.Button(bframe, text=' QUIT ')
btn.configure(command=lambda: menuCommand('E'))
btn.pack(side=tk.TOP)

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

txt = scrolledtext.ScrolledText(frame)
txt.configure(background='black', foreground='white')
txt.configure(font=('Cascadia Code PL', 10, 'normal'))
txt.configure(insertbackground='yellow', insertwidth=4)
txt.configure(wrap=tk.WORD)
txt.bind('<Tab>', tabsToSpaces)
txt.pack(fill=tk.BOTH, expand=1)

txt.focus()

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.mainloop()