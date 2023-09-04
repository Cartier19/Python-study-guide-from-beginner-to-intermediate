from datetime import date
date.today()
print(date.today())


parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")




#### sys arg
import sys
print(sys.argv)
print(sys.argv[0])


from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)
now = now + relativedelta(months = 1, weeks= 1, hour = 10)
print(now)
