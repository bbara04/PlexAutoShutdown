import datetime
import string
import sys
import os
import time

from notifytelegram import notify

with open('/home/bbara/PlexAutoShutdown/suspend', 'r') as readSuspend:
    line = readSuspend.readline().strip()
    last_suspend = datetime.datetime.strptime(line.strip(), '%Y.%m.%d %H:%M')

if (datetime.datetime.now() > last_suspend + datetime.timedelta(minutes=179)):
    print("shutdown")
    isSent = False
    tryCount = 0
    while isSent == False or tryCount >= 5:
        try:
            curdate = datetime.datetime.now()
            msg = str("Server has been shutdown at " + curdate.strftime('%H:%M'))
            isSent = notify(msg, "5499872795:AAGG2XQ-dbjkGZFIDYPdbvvdJa0XN6WYOHo", "5302671789")
        except:
            print("Couldn't send the telegram message")
            tryCount += 1
            time.sleep(20)
    open('/home/bbara/PlexAutoShutdown/uptime', 'w').write("shutdown")
    os.system('sudo shutdown now')
else :
    print("no shutdown")
