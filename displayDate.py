#Pedro Gallino
#11/15/17
#displayDate.py - displays the date, day of the week, month, and year


weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months = ['January','February','March','April','May','June','July','August','September','October','November','December' ]
today = datetime.date.today()
date = today.date
month = today.month
year = today.year
day = today.weekday()
print('Today is',weekdays[day],',',months[month],date,year)

