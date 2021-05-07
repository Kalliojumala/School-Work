#more datetime stuff
from datetime import datetime, timedelta

#first prog tells user how many days until christmas and 'vappu'(May 1st)
def christmas_and_mayfirst():
    date_now = datetime.now()
    christmas = datetime(date_now.year, 12, 24)
    vappu = datetime(date_now.year, 5, 1)

    if date_now > christmas:
        christmas += timedelta(days=365)
    #if date has passed, look for next year
    if date_now > vappu:
        vappu += timedelta(days=365)
    
    return (christmas - date_now).days , (vappu - date_now).days

###MAIN xd###
dates = christmas_and_mayfirst()
print(f"\nJouluun on {dates[0]} päivää ja vappuun on {dates[1]} päivää!")
print()

#second prog tells which one is closer to current date, summer- or wintersolstice
def solstices():
    date_now = datetime.now()
    wintersolstice = datetime(date_now.year, 12, 21)
    summersolstice = datetime(date_now.year, 6, 21)

    if date_now > wintersolstice:
        wintersolstice += timedelta(days=365)
    #if date passed look for next year 
    if date_now > summersolstice:
        summersolstice += timedelta(days=365)
    
    solstice_dates =   [(wintersolstice - date_now).days , (summersolstice - date_now).days]

    if solstice_dates[0] > solstice_dates[1]:
        return f'Summer solstice is closer to current date, {solstice_dates[1]} days away!\n'

    return f'Winter solstice is closer to current date, {solstice_dates[0]} days away!\n'

print(solstices())

