from datetime import datetime 
fday = input("first date: ")
sday = input("second date: ")
Fday = datetime.strptime(fday, '%Y-%m-%d %H:%M:%S')
Sday = datetime.strptime(sday, '%Y-%m-%d %H:%M:%S')
difference = (Sday - Fday).total_seconds()
print(abs(int(difference)))