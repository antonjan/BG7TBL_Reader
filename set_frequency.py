#!/usr/bin/python
import sys, serial

ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1) # Linux first FTDI
# sys.argv[1] is frequency in Herz
cmd = "\x8f" + "f" + '{:09d}'.format(int(sys.argv[1])/10)
ser.write(cmd)

