import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

root = tk.Tk()

def menuCommand(choice):
    pass

def updateStats(event):
    t = txt.get('1.0', 'end')
    t = t.replace('\n','')
    c = len(t)
    outStr = 'Stats: \n\n'
    outStr += '{:4>} chars'.format(c)
    l = int(txt.index('end').split('.')[0])-1
    outStr += '\n'
    outStr += '{:4>} lines'.format(l)
    mr = int(txt.index(tk.INSERT).split('.')[0])
    mc = int(txt.index(tk.INSERT).split('.')[1])+1
    outStr += '\n'
    outStr += '[r:{} c:{}]'.format(mr,mc)
    
    slbl.set(outStr)

# this is one way of changing tabs to spaces.
# THIS IS THE BEST METHOD, PROVIDES THE MOST CONSISTENT RESULTS.
# FROM THE EXAMPLES scrollmenu1..5
def tabsToSpaces(event):
    updateStats(event)
    mr = int(txt.index(tk.INSERT).split('.')[0])
    mc = int(txt.index(tk.INSERT).split('.')[1])+1
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

frame2 = tk.Frame(root)
frame2.pack(fill=tk.BOTH, expand=1)

slbl = tk.StringVar()
lbl = tk.Label(frame2)
lbl.configure(textvariable=slbl)
lbl.pack(fill=tk.BOTH, expand=1)

txt = scrolledtext.ScrolledText(frame)
txt.configure(background='black', foreground='white')
txt.configure(font=('Cascadia Code PL', 10, 'normal'))
txt.configure(insertbackground='yellow', insertwidth=4)
txt.bind('<Tab>', tabsToSpaces)
txt.bind('<KeyRelease>', updateStats)
txt.pack(fill=tk.BOTH, expand=1)

txt.focus()

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.mainloop()