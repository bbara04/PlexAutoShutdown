import json
import requests
import xml.etree.ElementTree as ET
import datetime


def log():
    try:
        # Get configuration from the config.json file
        config = json.load(open('/home/bbara/PlexAutoShutdown/config.json'))
        
        # Define the URL
        url = f"http://{config['ip']}:32400/status/sessions/?X-Plex-Token={config['plextoken']}"

        # Get the response from the URL
        response = requests.get(url)

        if response.status_code == 200:

            root = ET.fromstring(response.text)

            current_watching = None

            # Get current watchers
            for item in root.iter():
                if item.tag == 'MediaContainer':
                    current_watching = item.attrib['size']

            # Write current date to log file 
            # Format: (YYYY.MM.DD HH:MM)
            # Example: 2023.12.31 23:59
            if int(current_watching) > 0:
                open('/home/bbara/PlexAutoShutdown/log', 'w').write(datetime.datetime.now().strftime('%Y.%m.%d %H:%M'))

    except requests.exceptions.RequestException as e:
        print(e)
    except Exception as e:
        print(e)

log()
