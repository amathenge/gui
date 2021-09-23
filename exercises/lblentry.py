import tkinter as tk

root = tk.Tk()

s = tk.StringVar()
s.set('?')
lbl = tk.Label(root)
lbl.configure(font=('Cascadia Code PL', 14, 'normal'), height=5, width=30)
lbl.configure(textvariable=s, justify=tk.LEFT, anchor=tk.W)
lbl.grid(row=0, column=0, sticky=tk.EW)

def showText(event):
    v = txt.get()
    pos = 29
    lines = []
    while len(v) > pos:
        lines.append(v[:29])
        v = v[29:]
    lines.append(v)
    v = '\n'.join(lines)
    s.set(v)


txt = tk.Entry(root)
txt.configure(font=('Cascadia Code PL', 14, 'normal'))
txt.configure(background='black', foreground='yellow', insertbackground='yellow', insertwidth=16)
txt.bind('<KeyRelease>', showText)
txt.grid(row=1, column=0, sticky=tk.EW)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.mainloop()