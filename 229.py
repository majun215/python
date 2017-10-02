#!/usr/bin/python

from Tkinter import *
def hello(): print 'hello, world'
win = Tk()
win.title('hello, Tkinter!')
#win.geometry('200X100')

btn = Button(win,text = 'hello',command=hello)
btn.pack(expand=YES,fill=BOTH)

mainloop()
