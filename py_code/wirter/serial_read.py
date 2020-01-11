import serial 
import os
import datetime
today = datetime.date.today()
ser = serial.Serial('COM1',9600)
new_dir_mon = 'data_save/{}'.format(str(today.month()))
new_dir_day = 'data_save/{}'.format(str(today.day()))
new_dir_year = 'data_save/{}'.format(str(today.year()))
file = today.strftime("%d/%m/%y_%H:%M")
f = open("data_saved/list.txt","a")
for i in range(10):
    f.write("his is line {}".format(i))
    f.write("\n")
while ser.inWaiting():
    f.write(ser.read_until())
    f.write("\n")
