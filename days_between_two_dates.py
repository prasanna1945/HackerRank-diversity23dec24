from datetime import datetime
d1 = input()
d2 = input()
try:
    date1 = datetime.strptime(d1,"%d-%m-%Y")
    date2 = datetime.strptime(d2,"%d-%m-%Y")
    diff = abs(date1 - date2)
    print(diff.days)
except ValueError:
    print("ERROR")