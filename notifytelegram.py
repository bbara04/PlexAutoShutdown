import requests

def notify(message, token, chat_id):
    # Define the URL for the Telegram API
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    # Define the payload for the POST request
    payload = {
        'chat_id': chat_id,
        'text': message
    }

    try:
        # Make the POST request to the Telegram API
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Message sent successfully")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message: {e}")
        raise Exception("Failed to send message")
    