import requests
import json
import conf_reader

chat_id = conf_reader.read_conf_setting("conf.json", "chat_id")
api_token = conf_reader.read_conf_setting("conf.json", "api_token")


def prep_message(message, channel):
    """
    function creates message template for notification
    :param message:
    :param channel:
    :return:
    """
    group = channel["Group_name"]
    link = channel["URL"]
    time_attack = message.date
    msg = "\n🔴New Attack Has Been Detected!\n"
    msg += f"The group {group} at {time_attack} announced an attack:\n"
    msg += f"Text of the message: {message.text}\n"
    msg += f"Source: {link}\n"
    send_message(msg)


def send_message(text):
    """
    function sends prepared message
    :param text:
    :return:
    """
    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'
    json = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(api_url, json=json)