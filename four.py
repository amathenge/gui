#!/usr/bin/env python
#
# Calculator GUI
#
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# create the Tk() window
root = tk.Tk()
# set the window titlel
root.title("Tony's Calculator")
# set the width and height of the window
# root.geometry('400x400+0+0')
root.minsize(height=200, width=200) # should change this when app is ready.

# create a style for the calculator. The calculator will have 8 rows.
# row 1 = [input box] [=]
# row 2 = [1][2][3][+]
# row 3 = [4][5][6][-]
# row 4 = [7][8][9][*]
# row 5 = [(][0][)][/]
# row 6 = [memory][.]
# row 7 = [M][M+][CM][CA]
# row 8 = [MG]
# the last rows are memory options:
#   M = put the calculation into memory - clear existing memory calculation
#   M+ = add/append the calculation to existing memory calculation (+)
#   CM = clear memory
#   CA = clear memory and also calculation box
#   MG = get memory contents and put them in the calculation box
style = ttk.Style(root)
style.theme_use('clam')
style.configure('T1.TEntry', foreground='yellow', background='black', fieldbackground='black')
style.configure('T1.TEntry', insertcolor='blue', insertwidth=8)
# create the label
txt1 = ttk.Entry(root)
txt1.configure(font = ('Cascadia Code PL', 12, 'normal'), style='T1.TEntry')
# txt1.configure(state='disabled')
# Add the label to the grid at (0,0)
txt1.grid(row=0, column=0, columnspan=3, sticky=tk.E+tk.W+tk.S+tk.N, padx=5, pady=5)

# function to save the calculation to the box in row 6 [memory]
def buildCommand(item):
    txt = txt1.get()
    txt += str(item)
    txt1.delete(0,tk.END)
    txt1.insert(0, txt)

# function to calculate.
# txt1 has the calculation. Use Python's eval() function to calculate.
# display the answer in the same txt1 after an '=' sign.
def doMath():
    try:
        res = eval(txt1.get())
        res = str(res)
    except ZeroDivisionError:
        res = 'Error: [zero division]'
    except:
        res = 'Error: [Syntax]'
    txt = txt1.get()
    txt += '=' + res
    txt1.delete(0, tk.END)
    txt1.insert(0, txt)

# create a global variale to hold saved calculations [memory]
# memory buffer stuff.
# globals are bad, but we'll use them
mem = tk.StringVar()
mem.set('')

# function for row 6 - memory.
def memAction(action):
    # take the calculation and add it to memory - remove existing memory
    if action == 'M':
        txt = txt1.get()
        # remove the sum, if it's there in txt1 (calculation)
        while '=' in txt:
            txt = txt[0:txt.rfind('=')]
        # replace the content of the global memory variable with the calculation
        mem.set(txt)
    # add this calculation to the calculation already in memory.
    elif action == 'M+':
        tmp1 = mem.get()
        tmp2 = txt1.get()
        while '=' in tmp2:
            tmp2 = tmp2[0:tmp2.rfind('=')]
        tmp3 = tmp1 + '+(' + tmp2 + ')'
        mem.set(tmp3)
    # clear the memory
    elif action == 'CM':
        mem.set('')
    # clear the memory, and also clear the calculation box.
    elif action == 'CA':
        mem.set('')
        txt1.delete(0, tk.END)
    # get the contents of the memory and put them in the calculation box.
    elif action == 'MG':
        txt1.delete(0, tk.END)
        txt1.insert(0, mem.get())
    else:
        pass

# event listener - when the Return key on the keyboard is pressed, do the calculation.
# this supplments the "=" button.
def keyAction(event):
    if event.keysym == 'Return':
        doMath()

# this function will be bound to <Control-m> to add the calculation to memory
def keyMemory(event):
    memAction('M+')

# this function will be bound to <Control-c> to clear everything
def keyClear(event):
    memAction('CA')

# bind three keys to functions
# <KeyPress> = Return key
# <Control-m> = CTRL+M sequence
# <Control-c> = CTRL+C sequence
root.bind('<KeyPress>', keyAction)
root.bind('<Control-m>', keyMemory)
root.bind('<Control-c>', keyClear)

# create a style to be used for the buttons.
style = ttk.Style(root)
style.configure('B1.TButton', ipadx=10, height=50, width=5, justify='center', font=('Cascadia Code PL', 11, 'bold'))

# I don't quite remember why we create a 1x1 pixel image and add it to the button. I think it was for
# centering the text (hence the compound="center" option)
# equals button - next to entry box
# need pixel heights...
img1 = tk.PhotoImage(width=1, height=1)
btn1 = ttk.Button(root, text = '=', image=img1, compound='center', style='B1.TButton')
# btn1.configure(width=50, height=50)
btn1.configure(command=doMath)
btn1.grid(row=0, column=3, padx=5, pady=5)

# other buttons
btn2 = ttk.Button(root, text='1', image=img1, compound='center', style='B1.TButton')
# btn2.configure(width=50, height=50)
btn2.configure(command=lambda:buildCommand('1'))
btn2.grid(row=1, column=0, padx=5, pady=5)

btn3 = ttk.Button(root, text='2', image=img1, compound='center', style='B1.TButton')
# btn3.configure(width=50, height=50)
btn3.configure(command=lambda:buildCommand('2'))
btn3.grid(row=1, column=1, padx=5, pady=5)

btn4 = ttk.Button(root, text='3', image=img1, compound='center', style='B1.TButton')
# btn4.configure(width=50, height=50)
btn4.configure(command=lambda:buildCommand('3'))
btn4.grid(row=1, column=2, padx=5, pady=5)

btn5 = ttk.Button(root, text='+', image=img1, compound='center', style='B1.TButton')
# btn5.configure(width=50, height=50)
btn5.configure(command=lambda:buildCommand('+'))
btn5.grid(row=1, column=3, padx=5, pady=5)

btn6 = ttk.Button(root, text='4', image=img1, compound='center', style='B1.TButton')
# btn6.configure(width=50, height=50)
btn6.configure(command=lambda:buildCommand('4'))
btn6.grid(row=2, column=0, padx=5, pady=5)

btn7 = ttk.Button(root, text='5', image=img1, compound='center', style='B1.TButton')
# btn7.configure(width=50, height=50)
btn7.configure(command=lambda:buildCommand('5'))
btn7.grid(row=2, column=1, padx=5, pady=5)

btn8 = ttk.Button(root, text='6', image=img1, compound='center', style='B1.TButton')
# btn8.configure(width=50, height=50)
btn8.configure(command=lambda:buildCommand('6'))
btn8.grid(row=2, column=2, padx=5, pady=5)

btn9 = ttk.Button(root, text='-', image=img1, compound='center', style='B1.TButton')
# btn9.configure(width=50, height=50)
btn9.configure(command=lambda:buildCommand('-'))
btn9.grid(row=2, column=3, padx=5, pady=5)

btn10 = ttk.Button(root, text='7', image=img1, compound='center', style='B1.TButton')
# btn10.configure(width=50, height=50)
btn10.configure(command=lambda:buildCommand('7'))
btn10.grid(row=3, column=0, padx=5, pady=5)

btn11 = ttk.Button(root, text='8', image=img1, compound='center', style='B1.TButton')
# btn11.configure(width=50, height=50)
btn11.configure(command=lambda:buildCommand('8'))
btn11.grid(row=3, column=1, padx=5, pady=5)

btn12 = ttk.Button(root, text='9', image=img1, compound='center', style='B1.TButton')
# btn12.configure(width=50, height=50)
btn12.configure(command=lambda:buildCommand('9'))
btn12.grid(row=3, column=2, padx=5, pady=5)

btn13 = ttk.Button(root, text='*', image=img1, compound='center', style='B1.TButton')
# btn13.configure(width=50, height=50)
btn13.configure(command=lambda:buildCommand('*'))
btn13.grid(row=3, column=3, padx=5, pady=5)

btn14 = ttk.Button(root, text='(', image=img1, compound='center', style='B1.TButton')
# btn14.configure(width=50, height=50)
btn14.configure(command=lambda:buildCommand('('))
btn14.grid(row=4, column=0, padx=5, pady=5)

btn15 = ttk.Button(root, text='0', image=img1, compound='center', style='B1.TButton')
# btn15.configure(width=50, height=50)
btn15.configure(command=lambda:buildCommand('0'))
btn15.grid(row=4, column=1, padx=5, pady=5)

btn16 = ttk.Button(root, text=')', image=img1, compound='center', style='B1.TButton')
# btn16.configure(width=50, height=50)
btn16.configure(command=lambda:buildCommand(')'))
btn16.grid(row=4, column=2, padx=5, pady=5)

btn17 = ttk.Button(root, text='/', image=img1, compound='center', style='B1.TButton')
# btn17.configure(width=50, height=50)
btn17.configure(command=lambda:buildCommand('/'))
btn17.grid(row=4, column=3, padx=5, pady=5)

# use a label for the memory box (contents cannot be altered by typing them in)
lbl1 = ttk.Label(root, textvariable=mem)
lbl1.configure(font = ('Cascadia Code PL', 12, 'normal'))
lbl1.configure(foreground='yellow', background='black')
lbl1.grid(row=5, column=0, padx=5, pady=5, columnspan=3, sticky=tk.E+tk.W+tk.N+tk.S)

btn18 = ttk.Button(root, text='.', image=img1, compound='center', style='B1.TButton')
# btn18.configure(width=50, height=50)
btn18.configure(command=lambda:buildCommand('.'))
btn18.grid(row=5, column=3, padx=5, pady=5)

btn19 = ttk.Button(root, text='M', image=img1, compound='center', style='B1.TButton')
# btn19.configure(width=50, height=50)
btn19.configure(command=lambda:memAction('M'))
btn19.grid(row=6, column=0, padx=5, pady=5)

btn20 = ttk.Button(root, text='M+', image=img1, compound='center', style='B1.TButton')
# btn20.configure(width=50, height=50)
btn20.configure(command=lambda:memAction('M+'))
btn20.grid(row=6, column=1, padx=5, pady=5)

btn21 = ttk.Button(root, text='CM', image=img1, compound='center', style='B1.TButton')
# btn21.configure(width=50, height=50)
btn21.configure(command=lambda:memAction('CM'))
btn21.grid(row=6, column=2, padx=5, pady=5)

btn22 = ttk.Button(root, text='CA', image=img1, compound='center', style='B1.TButton')
# btn22.configure(width=50, height=50)
btn22.configure(command=lambda:memAction('CA'))
btn22.grid(row=6, column=3, padx=5, pady=5)

btn23 = ttk.Button(root, text='MG', image=img1, compound='center', style='B1.TButton')
# btn23.configure(width=50, height=50)
btn23.configure(command=lambda:memAction('MG'))
btn23.grid(row=7, column=0, padx=5, pady=5)


root.mainloop()
