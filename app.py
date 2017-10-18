from flask import Flask
import os
import requests

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
    :return: status code of the request
    """
    url = baseUrl + botPostMessageUrl + '?token=' + token
    json = {bot_id, text}
    response = requests.post(url, json=json)
    return response.status_code


@app.route('/')
def index():
    """
    All messages are sent to this URL and processed
    """
    return 'Yo, it\'s working!'


if __name__ == "__main__":
    app.run()
