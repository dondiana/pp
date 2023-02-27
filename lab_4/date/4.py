import datetime, time
x = datetime.datetime(2023, 2, 21).timetuple()
y = datetime.datetime(2023, 2, 20).timetuple()
z = time.mktime(x) - time.mktime(y)
print(z)