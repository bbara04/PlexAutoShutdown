#!/bin/bash

echo "shutdown" > /home/bbara/PlexAutoShutdown/uptime

TOKEN="5499872795:AAGG2XQ-dbjkGZFIDYPdbvvdJa0XN6WYOHo"
CHAT_ID="5302671789"
MESSAGE="(Manual) Server has been shutdown at $(date +'%H:%M')."

curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" -d chat_id=$CHAT_ID -d text="$MESSAGE"

sudo shutdown now
