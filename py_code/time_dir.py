import datetime
import os
import os.path
today = datetime.date.today()
mon = str(today.month)
day = str(today.day)
year = str(today.year)
year1 = today.strftime('%Y')
mon1 = today.strftime('%B')
day1 = today.strftime('%A')
file = today.strftime("%d-%m-%y__%H:%M")

try:
	os.mkdir('data_saved/{}'.format(year1))
except:
	print("year directory already exists")
try:
	os.mkdir('data_saved/{}/{}'.format(year1,mon1))
except:
	print("month directory already exists")
try:
	os.mkdir('data_saved/{}/{}/{}'.format(year1,mon1,day1))
except:
	print("day deractory already exists")

f = open('data_saved/{}/{}/{}/{}.txt'.format(year1, mon1, day1, file), "w+")
f.close()




