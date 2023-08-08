# Telegram Parser and Notifier
Script parses required Telegram Channels and sends Notification based on keywords to dedicated channel.

---
## Main Components
Consists from 2 parts:

**Telegram Bot** - sends notification to preconfigured channel

**Telegram App** - obtained through official Telegram API, used to parse Telegram Channels

---
## Components Description
**app_main.py** - main code to do whole job

**conf_pub.json** - configuration file

**conf_reader.py** - script to read configuration file

**message_work.py** - designated for message preparation and sending

**rss_work.py** - designated to work with RSS format and file

**rss_telebot.xml** - example of RSS feed file

---
## Inputs
Required inputs to **conf_pub.json** file:

**"chat_id": (str)** - chat ID designated to receive notifications, bot suppose to be a part of the channel

**"api_id": (int)** - application ID from Telegram API

**"api_hash": (str)** - application hash from Telegram API

**"username": (str)** - username to create connection profile (any username will fit)

**"minutes_relevancy": (int)** - minutes depth to pick up messages

**"rss_path": (str)** - path to RSS file

**"api_token": (str)** - Telegram Bot API token

**"ddos_wordslist": (list)** - list of words to track

**"telegram_channels": (list(dict))** - list of telegram channels to watch

---

![alt text](https://github.com/hyde1337/telegram-parse/blob/main/Telegram_Parser.png)

---
## Roadmap:
1. RSS Feed - DONE
2. Comprehensive logging
3. Dockerized version
4. MS Teams Integration 
TBC

---
## References:
1. https://docs.telethon.dev/en/stable/ - Telethon Docs
2. https://core.telegram.org - Telegram API
3. https://core.telegram.org/bots/tutorial - Telegram Bots and @BotFather