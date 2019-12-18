#!/usr/bin/python
import sys, serial
from Tkinter import *
#import tkinter as tk
import Tkinter as tk

window = tk.Tk()


def show_entry_fields():
    print("frequency: " (entryText.get()))
    entry.insert(window,10, 1234)


def sentd_frequency_to_LO():
    #ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)  # Linux first FTDI
    # sys.argv[1] is frequency in Herz
    '''cmd = "\x8f" + "f" + '{:09d}'.format(int(sys.argv[1])/10)'''

    cmd = "\x8f" + "f" + '{:09d}'.format(entrytext.get() / 10)
    # ser.write(cmd)
    print("frequency set to: ", entrytext.get())


def inc_freq(FreqChange):
    '''    assert isinstance(FreqChange, object)'''
    entry.insert(10, entrytext + FreqChange)
    entry.insert(10, FreqChange)
    ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)  # Linux first FTDI
    # sys.argv[1] is frequency in Herz
    '''cmd = "\x8f" + "f" + '{:09d}'.format(int(sys.argv[1])/10)'''
    entryText = txt.get()
    cmd = "\x8f" + "f" + '{:09d}'.format(int(entrytext) / 10)
    ser.write(cmd)



window.title("Es'hail-2 QA-100 Satellite Control")

window.geometry('640x400')
menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='New')

menu.add_cascade(label='File', menu=new_item)
entrytext = tk.IntVar()
entrytext.set(2400000000)
window.config(menu=menu)
# canvas = Canvas(window, height=400, width=640)
# canvas.pack()
lbl = Label(window, text="TX Freq Hz 2400000000")
lbl.pack()
'''lbl.grid(column=0, row=0)'''

entry = Entry(window, width=10, textvariable=entrytext)
entry.insert(10, "2400000000")
entry.pack()

'''txt.grid(column=1, row=0)'''


def clicked():
    lbl.configure(text="Button was clicked !!")

btn_change_freq = Button(window, text='Change Frequency', command=sentd_frequency_to_LO())
btn_change_freq.pack()
btn_exit = Button(window, text='Quit', command=window.quit)
btn_exit.pack()

window.mainloop()
