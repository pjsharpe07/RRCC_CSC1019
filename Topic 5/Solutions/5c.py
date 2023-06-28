# Between 06:01 and 12:00 is morning​
# Between 12:01 – 18:00 is afternoon​
# Between 18:01 – 00:00 is evening​
# Between 00:00 – 06:00 is night

time = input()

hour = int(time[:2])
minutes = int(time[3:])

### first convert hour to am or pm ###

if hour > 12: # subtract 12 to conver to AM/PM
    am_pm_hour = hour - 12
    setting = 'PM'
elif hour == 12: # no need to pad for zeros here
    am_pm_hour = 12
    setting = 'PM'
else: # pad for 0s
    am_pm_hour = '0' + str(hour)
    setting = 'AM'

### convert the time of day

if hour == 0 and minutes == 0:
    time_of_day = 'evening'
elif hour < 6:
    time_of_day = 'night'
elif hour >= 6 and hour < 12:
    if hour == 6 and minutes == 0:
        time_of_day = 'night'
    else:
        time_of_day = 'morning' 
elif hour >= 12 and hour < 18:
    if hour == 18 and minutes == 0:
        time_of_day = 'morning'
    else:
        time_of_day = 'afternoon'
else:
    time_of_day = 'evening'

print(f'This is the {time_of_day} and is {am_pm_hour}:{minutes:02} {setting}')