#!/usr/bin/python                             
'''https://sigrok.org/wiki/BG7TBL'''
import serial

ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1) # Linux first FTDI
ser.write("\x8f" + "v")
print("version is " + ser.read())
