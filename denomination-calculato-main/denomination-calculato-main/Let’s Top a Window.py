from tkinter import *

window=Tk()
window.geometry("400x300")
window.title("main")

def topwin():
    top=Toplevel()
    top.geometry("180x100")
    top.title("topwin")
    l2=Label(top,text="this is top window")
    l2.pack()
    top.mainloop()
l=Label(window,text="this is root window")
btn=Button(window,text="click here to open window",command=topwin)
l.pack()
btn.pack()
window.mainloop()