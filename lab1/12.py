import datetime
n = int(input("Enter the time zone off set to GEM: "))
GMT_FORMAT = '%H:%M:%S'
print("The current time is "+(datetime.datetime.utcnow()-datetime.timedelta(hours=n)).strftime(GMT_FORMAT))