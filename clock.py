import os
import requests
from apscheduler.schedulers.background import BackgroundScheduler

bot_id = os.getenv('BOT_ID', '')  # second variable is default, nothing
token = os.getenv('USER_TOKEN', '')

scheduler = BackgroundScheduler(timezone="EDT")

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
    return post_message_to_group('Anyone taken the trash out?')


scheduler.add_job(remind_group, 'cron', day_of_week='mon,thu', hour=17)
scheduler.add_job(remind_group, 'cron', day_of_week='tue,fri', hour=8)

if __name__ == '__main__':
    scheduler.start()
