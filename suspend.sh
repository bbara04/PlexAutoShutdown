#!/bin/bash

# Get formatted date
formatted_date=$(date '+%Y.%m.%d %H:%M')

# Define the output file
output_file="/home/bbara/PlexAutoShutdown/suspend"

# Write the current date to the file
echo "$formatted_date" > "/home/bbara/PlexAutoShutdown/suspend"

echo "suspend" > "/home/bbara/PlexAutoShutdown/uptime"

sudo rtcwake -u -s 10800 -m mem && /usr/bin/python3 /home/bbara/PlexAutoShutdown/afterSuspend.py
