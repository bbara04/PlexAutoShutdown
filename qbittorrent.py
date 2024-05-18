import os
import requests
import json

# Define the paths and credentials
cookie_jar_path = os.path.expanduser('~/.cookies.txt')

def isFileDownloading(ip, username, password):
    # Define paths and URLs
    login_url = f"http://{ip}:8080/api/v2/auth/login"
    torrents_info_url = f"http://{ip}:8080/api/v2/torrents/info"

    # Remove existing cookie jar
    if os.path.exists(cookie_jar_path):
        os.remove(cookie_jar_path)

    # Create a session to persist cookies
    session = requests.Session()

    # Login to qbittorrent
    login_payload = {
        'username': username,
        'password': password
    }
    login_headers = {
        'Referer': f"http://{ip}:8080"
    }
    response = session.post(login_url, data=login_payload, headers=login_headers)
    response.raise_for_status()

    # Get list of downloading torrents
    torrents_response = session.get(torrents_info_url, headers=login_headers)
    torrents_response.raise_for_status()

    # Parse the response JSON
    torrents_info = torrents_response.json()

    # Check torrent states
    states_to_check = {"stalledDL", "downloading", "metaDL"}
    is_downloading = any(torrent['state'] in states_to_check for torrent in torrents_info)

    # Clean up: remove cookie jar if you want to
    # (session keeps cookies in memory, so you don't need to handle a file)
    session.cookies.clear()

    return is_downloading
