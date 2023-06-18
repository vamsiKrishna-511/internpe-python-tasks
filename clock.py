from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Digital Clock')


def time():
    string = strftime('%I:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('courier', 35, 'bold'),
            background='lightskyblue',
            foreground='white')


lbl.pack(anchor='center')
time()

mainloop()