import json
import os
import datetime
import string
import sys
import subprocess

from qbittorrent import isFileDownloading
from notifytelegram import notify
from log import log

path = "/home/bbara/PlexAutoShutdown"

# Check watch state
log()

# Get configuration from the config.json file
config = json.load(open('/home/bbara/PlexAutoShutdown/config.json'))


# Get the uptime of the system
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    return uptime_seconds

# Get last time content has been watched
with open('/home/bbara/PlexAutoShutdown/log', 'r') as f:
    line = f.readline()
    last_watched = datetime.datetime.strptime(line.strip(), '%Y.%m.%d %H:%M')


# Handle uptime

uptime = -1

with open('/home/bbara/PlexAutoShutdown/uptime', 'r') as uptimefile:
    line = uptimefile.readline().strip()
    if (line == 'shutdown'):
        open(os.path.join(path, 'uptime'), 'w').write('0')
        sys.exit(0)
    elif (line == 'suspend'):
        open(os.path.join(path, 'uptime'), 'w').write(str(get_uptime()))
        sys.exit(0)
    else:
        try:
            uptime = float(line)
        except:
            uptime = -1

# If uptime is less than the specified time, exit
if(uptime == -1):
    print("Uptime file format is wrong")
    sys.exit(0)
else:
    if((get_uptime()-uptime)<(int(sys.argv[1])*60)):
        print("uptime kisebb " + str(round(get_uptime()-uptime, 1)) + ' sec')
        sys.exit(0)

# If conent is currently being downloaded, exit
try:
    if(config['watchdownloads'] == True and isFileDownloading(config['ip'], config['qbittorrent']['username'], config['qbittorrent']['password'])):
        sys.exit(0)
except:
    print("Couldn't get response from qbittorrent client")

# If the last watched content is older than the specified time, shutdown or hibernate the system
if(datetime.datetime.now() - last_watched > datetime.timedelta(minutes=int(sys.argv[1]))):
    curdate = datetime.datetime.now()
    msg = str("Server has been suspended at " + curdate.strftime('%H:%M'))
    notify(msg, config['telegram']['token'], config['telegram']['chat_id'])
    print('suspend')
    subprocess.run(['bash', os.path.join(path, "suspend.sh")], capture_output=False, text=True)
