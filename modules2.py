import datetime
from datetime import *

x=datetime.now()
print(x)

print(date(2001,12,7))

print("Today's date", date.today())

now = datetime.now()
time = now.strftime("%H:%M:%S")
print("Time:", time)
print(now.strftime("%B"))
print(now.strftime("%A"))