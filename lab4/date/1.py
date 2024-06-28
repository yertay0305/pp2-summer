from datetime import date, timedelta
fda = date.today() - timedelta(5)
print("Current day: ", date.today())
print("Five days ago: ", fda)