#!/usr/bin/python
import sys, serial
from tkinter import *

def show_entry_fields():
   '''print("frequency: " (txt.get()))'''
   txt.insert(10,"2400000000")

def sentd_frequency_to_LO():
    ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1) # Linux first FTDI
    # sys.argv[1] is frequency in Herz
    '''cmd = "\x8f" + "f" + '{:09d}'.format(int(sys.argv[1])/10)'''
    entryText = txt.get()
    cmd = "\x8f" + "f" + '{:09d}'.format(int(entryText)/10)
    ser.write(cmd)



window = Tk()

window.title("Es'hail-2 QA-100 Satellitei Controle")

window.geometry('640x400')
menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='New')

menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)

lbl = Label(window, text="Transmitting Frequency n Hz EG 2400000000")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.insert(10,"2400000000")


txt.grid(column=1, row=0)

def clicked():

    '''    lbl.configure(text="Button was clicked !!")'''

btn = Button(window)

btn.grid(column=3, row=0)
Button(window, text='Quit', command=window.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(window, text='Set Frequency: ', command=sentd_frequency_to_LO).grid(row=3, column=1, sticky=W, pady=4)
Button(window, text='Get Frequency: ', command=show_entry_fields).grid(row=3, column=2, sticky=W, pady=4)

window.mainloop()
