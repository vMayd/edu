# -*- coding: utf-8 -*-
'''
Tkinkter test
'''
from Tkinter import *

root = Tk()
label = Label(root, text="Hello! What is your name?", font=("Helvetica", "14"))
label.grid(row=0, column=0)
input1 = Text(root, height=1, font=("Helvetica", "14"))
input1.grid(row=1, column=0)
var = StringVar()
output = Label(root,textvariable=var, font=("Helvetica", "14"))
output.grid(row=2, column=0)

def hello():
    text = input1.get("1.0", END)
    text = str(text).replace('\n', '')
    if text.lower() == 'toma':
        var.set('Hello, {0}. Glad that you are at home already!'.format(text))
    elif text.lower() == 'vova':
        var.set('Hello, {0}. Let someone else to try.'.format(text))
    else:
        var.set('Hello, {0}!'.format(text))

button = Button(root, text='Push me, baby!', height=1, command=hello)
button.grid(row=1, column=2)

root.mainloop()
