# -*- coding: utf-8 -*-
'''
Задание 1
Даны две строки. Выведите на экран символы, которые есть в обоих строках.
'''

from Tkinter import *
root = Tk()
text1 = Text(root,font=("Helvetica",14),width=50, height=2)
text2 = Text(root,font=("Helvetica",14),width=50, height=2)


def func():
    str1 = set(str(text1.get("1.0",END)).lower().replace(' ',''))
    str2 = set(str(text2.get("1.0",END)).lower().replace(' ',''))
    ou_str = str1.intersection(str2)
    _str = ''

    for l in ou_str:
        _str += l+' '

    _str = _str.replace('\n','')
    text3.delete("1.0", END)
    text3.insert(INSERT, _str)
label = Label(root, text = 'Here is common leters:')
btn = Button(root,text="Check", command = func)
text3 = Text(root,font=("Helvetica",14),width=50, height=2)

text1.pack()
text2.pack()
label.pack()
text3.pack()
btn.pack()

root.mainloop()

