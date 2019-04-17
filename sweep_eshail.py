#!/usr/bin/python
import sys, serial
import time
ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1) # Linux first FTDI
# sys.argv[1] is frequency in Herz
# cmd = "\x8f" + "f" + '{:09d}'.format(int(sys.argv[1])/10)
# ser.write(cmd)
while True:
	print "Frequensy set to "
	for a in range(2254900000,2254900100,5):
		time.sleep( 0.1 )
                cmd = "\x8f" + "f" + '{:09d}'.format(int(a)/10)
                ser.write(cmd)
  		print(a)
	for a in range(2254900100,2254900000,-5):
		time.sleep( 0.1 )
                cmd = "\x8f" + "f" + '{:09d}'.format(int(a)/10)
                ser.write(cmd)
  		print(a)

