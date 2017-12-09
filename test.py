from reminderBot import reminder_bot
import datetime

print(datetime.datetime.now())

while 1:
    alarm = reminder_bot()
    if alarm != "no-alarm":
        print(alarm)
