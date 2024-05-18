# Shutdown script

The goal of this project is to automatically shut down the server, taking into account when content was last viewed or if a download is in progress at the moment. Notifications about this can also be received via Telegram.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)
- plex token (https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/)

## Project Setup
#### Clone the repository
```bash
git clone https://your-repo-url.git
```

#### Change Directory to repo
```bash
cd PlexAutoShutdown
```

#### Install Dependecies
```bash
pip install -r requirements.txt
```

#### Give required permissions
```bash
sudo chmod 776 ./*
```

## Configuration

To configure the config file, follow these steps:

1. Open the `config.yaml` file located in the project directory.
2. Modify the necessary settings according to your requirements.
3. Save the changes and close the file.

```json
{
    "ip": "localhost",  Ip address of your server
    "plextoken": "plex token",    Plex token
    "watchdownloads": true, Set true if you don't want your server to turnoff while downloading content
    "qbittorrent": {
        "username": "username",    QBittorrent username
        "password": "password"    QBittorrent password
    },
    "notification": true,   Set true if you want to be notified about the system shutting down
    "telegram": {
        "token": "token",  Telegram token
        "chat_id": "chat_id" Telegram Chat_id
    }
}
```

Ensure that you have set all required parameters in the config file before running the scripts.

## Usage

To run these scripts periodically, you can set up a cron job. Here's how you can configure cron jobs:

#### Open the cron table
```bash
crontab -e
```

#### Add cron jobs

By default, the scripts are run every 60 minutes, but this can be changed by providing an argument to `shutdown.py`.

```bash
*/3 * * * * /usr/bin/python3 /path/to/file/log.py
*/6 * * * * /usr/bin/python3 /path/to/file/shutdown.py 60
```
