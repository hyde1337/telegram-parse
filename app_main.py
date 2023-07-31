import time
import requests
from telethon.sync import TelegramClient
import datetime
import message_work
import json
import conf_reader

username = conf_reader.read_conf_setting("conf.json", "username")
api_id = conf_reader.read_conf_setting("conf.json", "api_id")
api_hash = conf_reader.read_conf_setting("conf.json", "api_hash")
telegram_channels = conf_reader.read_conf_setting("conf.json", "telegram_channels")

def connect_telegram_app(channels):
    for channel in channels:
        print(f"proceeding channel {channel}")
        with TelegramClient(username, api_id, api_hash) as client:
            for message in client.iter_messages(channel["URL"], limit=6):
                print(message)
                message_context(message, channel)


def message_context(message, channel):
    ddos_wordslist = conf_reader.read_conf_setting("conf.json", "ddos_wordslist")
    if message.forward is None and message.text is not None:
        message_lower = message.text.replace("\n", " ").lower()
        for word in ddos_wordslist:
            print(f"word check {word}")
            if word in message_lower and check_date(message.date):
                print(message_lower)
                message_work.prep_message(message, channel)
    else:
        print("No suitable messages were found")


def check_date(date_in):
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
