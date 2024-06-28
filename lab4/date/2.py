from datetime import date, timedelta
y = date.today() - timedelta(1)
t = date.today() + timedelta(1)
print("Yesterday: ", y)
print("Today: ", date.today())
print("Tomorrow: ", t)