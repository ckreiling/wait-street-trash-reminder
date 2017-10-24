from flask import Flask
import os
import requests
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

bot_id = os.getenv('BOT_ID', '')  # second variable is default, nothing
token = os.getenv('USER_TOKEN', '')


@app.route('/', methods=['POST'])
def index():
    """
    All messages from the group are sent to this URL, the response structure is:
    {
      "attachments": [],
      "avatar_url": "https://i.groupme.com/123456789",
      "created_at": 1302623328,
      "group_id": "1234567890",
      "id": "1234567890",
      "name": "John",
      "sender_id": "12345",
      "sender_type": "user",
      "source_guid": "GUID",
      "system": false,
      "text": "Hello world ☃☃",
      "user_id": "1234567890"
    }
    """

    return 'Got the message!'


if __name__ == "__main__":
    app.run()
