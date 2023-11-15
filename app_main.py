import time
import requests
from telethon.sync import TelegramClient
import datetime
import message_work
import json
import conf_reader
import rss_work

username = conf_reader.read_conf_setting("conf.json", "username")
api_id = conf_reader.read_conf_setting("conf.json", "api_id")
api_hash = conf_reader.read_conf_setting("conf.json", "api_hash")
telegram_channels = conf_reader.read_conf_setting("conf.json", "telegram_channels")

def connect_telegram_app(channels):
    """
    function to connect to Telegram API
    """
    for channel in channels:
        print(f"proceeding channel {channel}")
        try:
            with TelegramClient(username, api_id, api_hash) as client:
                for message in client.iter_messages(channel["URL"], limit=6):
                    print(message)
                    message_context(message, channel)
        except:
            print(f"the channel {channel} is not available")
            pass


def message_context(message, channel):
    """
    function to check presence of any word in the word list in the message
    :param message:
    :param channel:
    :return:
    """
    ddos_wordslist = conf_reader.read_conf_setting("conf.json", "ddos_wordslist")
    if message.forward is None and message.text is not None:
        message_lower = message.text.replace("\n", " ").lower()
        for word in ddos_wordslist:
            print(f"word check {word}")
            if word in message_lower and check_date(message.date):
                #print(message_lower)
                message_work.prep_message(message, channel)
                rss_work.write_rss(message, channel)
    else:
        print("No suitable messages were found")


def check_date(date_in):
    """
    function to check the date of the message
    :param date_in:
    :return:
    """
    minutes_relevancy = conf_reader.read_conf_setting("conf.json", "minutes_relevancy")
    now = datetime.datetime.utcnow() - datetime.timedelta(minutes=minutes_relevancy)

    if date_in.replace(tzinfo=None) > now.replace(tzinfo=None):
        print(f"Date passed is {now}")
        return True
    else:
        print(f"Date failed is {now}")
        return False


def main():
    connect_telegram_app(telegram_channels)


if __name__ == "__main__":
    main()
