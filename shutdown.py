import json
import os
import datetime
import string
import sys
import subprocess

from qbittorrent import isFileDownloading
from notifytelegram import notify

# Get configuration from the config.json file
config = json.load(open('./config.json'))


# Get the uptime of the system
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    return uptime_seconds

# Get last time content has been watched
with open('./log', 'r') as f:
    line = f.readlines()[-1]
    
    last_watched = datetime.datetime.strptime(line, '%Y.%m.%d %H:%M')


# If uptime is less than the specified time, exit
if(get_uptime()<(int(sys.argv[1])*60)):
    sys.exit(0)

# If conent is currently being downloaded, exit
if(config['watchdownloads'] == False or isFileDownloading(config['ip'], config['qbittorrent']['username'], config['qbittorrent']['password'])):
    sys.exit(0)

# If the last watched content is older than the specified time, shutdown or hibernate the system
if(datetime.datetime.now() - last_watched > datetime.timedelta(minutes=int(sys.argv[1]))):
    if(sys.argv[2] == 'shutdown'):
        os.system('sudo shutdown')
        if(config['notification'] == True):
            notify('Server has been powered off', config['telegram']['token'], config['telegram']['chat_id'])
    elif(sys.argv[2] == 'suspend'):
        os.system('sudo systemctl suspend')

    