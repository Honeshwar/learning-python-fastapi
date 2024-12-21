import datetime

# x = datetime.datetime.now()
# print(x)
print("--------------")

# Common Methods:

# datetime.datetime.now(): Returns the current local date and time.
print(datetime.datetime.now())
print("--------------")

# datetime.date(year, month, day): Creates a date object for the specified year, month, and day.
print(datetime.date(2023, 1, 1))
print("--------------")

# datetime.timedelta(days, seconds, ...: Represents a duration (useful for date arithmetic).
print(datetime.timedelta(days=1))
print("--------------")

# datetime.datetime.strptime(string, format): Converts a string to a datetime object using a specified format.
print(datetime.datetime.strptime('2023-01-01', '%Y-%m-%d'))
print("--------------")

# datetime.datetime.strftime(format): Converts a datetime object to a string using a specified format.
print(datetime.datetime.now().strftime('%Y-%m-%d'))
print(datetime.datetime.now().strftime('%H:%M:%S'))
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("--------------")