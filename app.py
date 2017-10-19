from flask import Flask
import os
import requests
import schedule

app = Flask(__name__)

bot_id = os.getenv('BOT_ID', '')  # second variable is default, nothing
token = os.getenv('USER_TOKEN', '')

"""
Base URL for Groupme's API
"""
baseUrl = 'https://api.groupme.com/v3'

"""
Post material:
    - bot_id: ID for the bot
    - text: text for the bot to send to the group
"""
botPostMessageUrl = '/bots/post'


def post_message_to_group(text):
    """
    Posts a message to the group
    :param text: message to be posted to group
    :return: response object from the post request
    """
    url = baseUrl + botPostMessageUrl + '?token=' + token
    json = {bot_id, text}
    response = requests.post(url, json=json)
    return response


def remind_group():
    return post_message_to_group('Y\'all taken the trash out yet?')


schedule.every().monday.at('17:00').do(remind_group)
schedule.every().tuesday.at('08:00').do(remind_group)
schedule.every().thursday.at('17:00').do(remind_group)
schedule.every().friday.at('08:00').do(remind_group)


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

    return 200


if __name__ == "__main__":
    app.run()
