import serial 
import os
ser = serial.Serial('COM1',9600)

f = open("lists.txt","a")
for i in range(10):
    f.write("his is line {}".format(i))
    f.write("\n")
while ser.inWaiting():
    f.write(ser.read_until())
    f.write("\n")
