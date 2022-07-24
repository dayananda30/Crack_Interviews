from datetime import date

"""
Get Current Date
"""
today = date.today()
print("Today's date is", today)

###########################################
"""
 Get Today’s Year, Month, and Date
"""
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#############################################
"""
Get date from Timestamp
"""
from datetime import datetime

# Getting Datetime from timestamp
date_time = datetime.fromtimestamp(1887639468)
print("Datetime from timestamp:", date_time)

###############################################
"""
Convert Date to String
"""
from datetime import date
today = date.today()
# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)
print(type(Str))

################################################


