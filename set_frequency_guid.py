#!/usr/bin/python
import sys, serial
from tkinter import *

window = Tk()


def show_entry_fields():
    '''print("frequency: " (txt.get()))'''
    txt.insert(10, Frequency)


def sentd_frequency_to_LO():
    ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)  # Linux first FTDI
    # sys.argv[1] is frequency in Herz
    '''cmd = "\x8f" + "f" + '{:09d}'.format(int(sys.argv[1])/10)'''
    entryText = txt.get()
    cmd = "\x8f" + "f" + '{:09d}'.format(int(entryText) / 10)
    ser.write(cmd)


def inc_freq(FreqChange):
    '''    assert isinstance(FreqChange, object)'''
    txt.insert(10, txt.get() + FreqChange)
    txt.insert(10, frequency)
    ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)  # Linux first FTDI
    # sys.argv[1] is frequency in Herz
    '''cmd = "\x8f" + "f" + '{:09d}'.format(int(sys.argv[1])/10)'''
    entryText = txt.get()
    cmd = "\x8f" + "f" + '{:09d}'.format(int(Frequency) / 10)
    ser.write(cmd)


FUB = 1000
FUBB = 10000
FUBBB = 100000
FDN = -1000
FDNN = -10000
FDNNN = -100000
Frequency = 2400000000


window.title("Es'hail-2 QA-100 Satellite Control")

window.geometry('640x400')
menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='New')

menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)
'''canvas = Canvas(window, height=400, width=640)
canvas.pack()'''
lbl = Label(window, text="TX Freq Hz 2400000000")
lbl.pack()
'''lbl.grid(column=0, row=0)'''

txt = Entry(window, width=10)
txt.insert(10, "2400000000")
txt.pack()
'''txt.grid(column=1, row=0)'''


def clicked():
    lbl.configure(text="Button was clicked !!")


btn = Button(window, text='Quit', command=window.quit)
btn.pack()
window.mainloop()
