# -*- coding:utf-8 -*-
import tkinter
root = tkinter.Tk()
label = tkinter.Label(root,text="hello,tkinter")
label.pack()
button1 = tkinter.Button(root,text="提交")
button1.pack(side=tkinter.LEFT)
button2 = tkinter.Button(root,text="取消")
button2.pack(side=tkinter.RIGHT)
root.mainloop()
