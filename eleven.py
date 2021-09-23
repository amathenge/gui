#!/usr/bin/env python
#
# Exercises on using Tcl/Tk
#
import tkinter as tk
from tkinter import messagebox
#
# button = tk.Button(root)
# text box = tk.Entry(root)
# label = tk.Label(root)
#
root = tk.Tk()

'''
Globals
'''
str1 = tk.StringVar()   # for the edit box.

def intList(item):
    tmp = []
    for element in item:
        try:
            element = int(element)
            tmp.append(element)
        except:
            pass
    if len(tmp) == len(item):
        return tmp
    else:
        return None

'''
Callbacks
'''
def drawShape():
    s = str1.get()
    if len(s) < len('type(1,2,3,4)'):
        messagebox.showinfo('Error', "input error: {}".format(s))
    else:
        cmd = s[0:4].lower()
        if cmd not in ('line', 'rect', 'oval', 'poly', 'circ'):
            messagebox.showinfo('Error', "input error: {}".format(s))
            return None
        cmd1 = s[4:]
        pos1 = cmd1.find('(')
        if pos1 == -1:
            messagebox.showinfo('Error', "input error: {}".format(s))
            return None
        pos2 = cmd1.rfind(')')
        if pos2 == -1:
            messagebox.showinfo('Error', "input error: {}".format(s))
            return None
        # if we're here, we may have good data.
        data = cmd1[pos1+1:pos2]
        # messagebox.showinfo('Data', 'you have {}, {}'.format(cmd, data))
        # now checking.
        if cmd == 'line':
            points = data.split(',')
            points = intList(points)
            if points == None:
                messagebox.showinfo('Error', 'Invalid data: {}'.format(data))
                return None
            if len(points) != 4:
                messagebox.showinfo('Error', 'Invalid number of points: {}'.format(data))
                return None
            line = c.create_line(points[0],points[1],points[2],points[3])
            c.itemconfig(line, fill='blue', width=2)
        if cmd == 'rect':
            points = data.split(',')
            points = intList(points)
            if points == None:
                messagebox.showinfo('Error', 'Invalid data: {}'.format(data))
                return None
            if len(points) != 4:
                messagebox.showinfo('Error', 'Invalid number of points: {}'.format(data))
                return None
            rect = c.create_rectangle(points[0],points[1],points[2],points[3])
            c.itemconfig(rect, outline='green', width=2)
        if cmd == 'circ':
            points = data.split(',')
            points = intList(points)
            if points == None:
                messagebox.showinfo('Error', 'Invalid data: {}'.format(data))
                return None
            if len(points) != 3:
                messagebox.showinfo('Error', 'Invalid number of points: {}'.format(data))
                return None
            boundingbox = [points[0], points[1], points[0]+points[2], points[1]+points[2]]
            circle = c.create_oval(boundingbox[0],boundingbox[1],boundingbox[2],boundingbox[3])
            c.itemconfig(circle, outline='red', width=2)

frame1 = tk.Frame(root, highlightcolor='blue', highlightthickness=2, bd=0)
frame1.pack(fill = tk.BOTH, expand = True)
frame2 = tk.Frame(root)
frame2.pack(fill = tk.BOTH, expand = True)
frame3 = tk.Frame(root)
frame3.pack(fill = tk.BOTH, expand = True)

# text box and a single button in the first frame.
# canvas in the second frame
# label with instructions in the third frame

txt1 = tk.Entry(frame1, width = 25, textvariable = str1, foreground = 'yellow', background = 'black')
txt1.configure(insertbackground = 'white', insertwidth = 4)
txt1.configure(font = ('Comic Sans', 12, 'normal'))
txt1.pack(side = tk.LEFT, padx = 20, pady = 20)

img = tk.PhotoImage(width = 1, height = 1)
btn1 = tk.Button(frame1, text = " Draw ", image = img, width=100, height=30)
btn1.configure(font = ('Comic Sans', 11, 'bold'), compound = 'center')
btn1.configure(foreground = 'blue')
btn1.configure(command = drawShape)
btn1.pack(side = tk.LEFT, padx = 40)

c = tk.Canvas(frame2)
c.pack(fill = tk.BOTH, expand = True, padx = 4, pady = 4)
c.config(width = 640, height = 400)
c.config(borderwidth = 0, highlightthickness = 0)

str2 = 'How to draw objects on the canvas above:\n'
str2 += "for a circle: ->  circ: (x,y,r) [where x,y are coordinate, r is radius]\n"
str2 += "for an oval: -> oval: (x,y,x2,y2) [bounding box]\n"
str2 += "for a rect: ->  rect: (x,y,x2,y2) [bounding box]\n"
str2 += "for a line: -> line: similar to rect\n"
str2 += "for a polygon: ->  poly: (x,y,x2,y2,x3,y3...) - must be at least 3 pairs\n"
lbl1 = tk.Label(frame3, text = str2)
lbl1.configure(font = ('Courier New', 12, 'normal'))
lbl1.configure(anchor = tk.NW, justify = tk.LEFT, relief = tk.GROOVE, borderwidth = 2)
lbl1.configure(padx = 10, pady = 5)
# when the parent is stretched, the label will stick to the left side.
lbl1.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
'''
  fill option: it determines whether to use up more space or keep "one's own" dimensions.
  expand option: it deals with the expansion of parent widget.
'''
txt1.focus()

root.mainloop()
