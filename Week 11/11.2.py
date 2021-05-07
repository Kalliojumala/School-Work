#datetime excercises
from datetime import datetime

###EXC 1###

#example date used in the two formatting missions.
date_ex = datetime(2028,10,23,17,39,10)

#list of formats for time of day
time_formats = ['%I:%M:%S %p', '%H:%M:%S', '%H.%M.%S' ]

#print three asked formats
print('Excercise One:\n')
for i in time_formats:
    print(date_ex.strftime(i))

print()

### EXC 2###
#list of formats for date
date_formats = ['%b %d, %Y', '%m/%d/%y', '%d/%B/%Y', '%A %B %d', '%d.%m.%Y']

#print loop
print('Excercise Two: \n')
for i in date_formats:
    print(date_ex.strftime(i))
print()

#write a prog that asks for birthday and return day of week
def birthweekday():
    user_input = input("Syötä syntymäpäiväsi: ").split('.')
    birthdate = datetime(int(user_input[2]),int(user_input[1]),int(user_input[0]))

    #dict to convert day of week to finnish, there might be a better way of doing this :D
    weekdays_finnish = {'Monday':'Maanantai', 'Tuesday':'Tiistai', 'Wednesday':'Keskiviikko', 'Thursday':'Torstai', 'Friday':'Perjantai', 'Saturday':'Lauantai'}
    
    #loop over dict comparing birthdates day of week, return value(finnish day of week) if its a match, else function returns sunday
    for keys,values in weekdays_finnish.items():
        if birthdate.strftime('%A') == keys:
            return values
    return 'Sunnuntai'


print(birthweekday())
