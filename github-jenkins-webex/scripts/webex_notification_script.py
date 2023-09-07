#!/usr/bin/env python

import subprocess
import requests
import sys

# Replace with your Webex Teams API token and room ID
WEBEX_TEAMS_API_TOKEN = ''
WEBEX_ROOM_ID = ''

# Function to send a Webex Teams message
def send_webex_teams_message(message):
    # Headers for the Webex API request
    headers = {
        "Authorization": f"Bearer {WEBEX_TEAMS_API_TOKEN}",
        "Content-Type": "application/json"
    }

    # Payload for the Webex API request
    data = {
        "roomId": WEBEX_ROOM_ID,
        "markdown": message
    }

    # Webex API endpoint for sending messages
    WEBEX_API_URL = "https://webexapis.com/v1/messages"

    # Send the message to the Webex room
    response = requests.post(WEBEX_API_URL, json=data, headers=headers)

    # Check if the message was sent successfully
    if response.status_code == 200:
        print("Webex notification sent successfully.")
    else:
        print(f"Failed to send Webex notification. Status code: {response.status_code}")
        print("Response content:", response.text)

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <message>".format(sys.argv[0]))
        sys.exit(1)

    message = sys.argv[1]

    try:
        # Send the provided message to Webex Teams
        send_webex_teams_message(message)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
