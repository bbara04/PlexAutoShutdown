import json
import requests
import xml.etree.ElementTree as ET
import datetime

# Get configuration from the config.json file
config = json.load(open('/home/bbara/PlexAutoShutdown/config.json'))

# Define the URL
url = f"http://{config['ip']}:32400/status/sessions/history/all?sort=viewedAt:desc&X-Plex-Container-Start=0&X-Plex-Container-Size=1&X-Plex-Token={config['plextoken']}"

# Get the response from the URL
response = requests.get(url)

print(response.text)

root = ET.fromstring(response.text)

# Get current watchers
for item in root.iter():
    if item.tag == 'MediaContainer':
        current_watching = item.attrib['size']