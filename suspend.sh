#!/bin/bash

# Get formatted date
formatted_date=$(date '+%Y.%m.%d %H:%M')

# Define the output file
output_file="/home/bbara/PlexAutoShutdown/suspend"

# Write the current date to the file
echo "$formatted_date" > "/home/bbara/PlexAutoShutdown/suspend"

echo "suspend" > "/home/bbara/PlexAutoShutdown/uptime"

TOKEN="7634927453:AAHKziilCwPPLub2iFAUESttmAqqDY4pZPQ"
CHAT_ID="5302671789"
MESSAGE="Server has been suspended at $(date +'%H:%M')"

curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" -d chat_id=$CHAT_ID -d text="$MESSAGE"

sudo rtcwake -u -s 10800 -m mem && /usr/bin/python3 /home/bbara/PlexAutoShutdown/afterSuspend.py
