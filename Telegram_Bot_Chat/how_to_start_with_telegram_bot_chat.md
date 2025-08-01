# How to start with Telegram Bot Chat 

**Content :**
1. [Create Telegram Bot](#create-a-telegram-bot-and-get-a-bot-token)
    1. [Create a Telegram Bot and get a Bot Token](#create-a-telegram-bot-and-get-a-bot-token)
    1. [Get Chat ID for a Private Chat](#get-chat-id-for-a-private-chat)
    1. [Get Chat ID for a Channel](#get-chat-id-for-a-channel)
    1. [Get Chat ID for a Group Chat](#get-chat-id-for-a-group-chat)
    1. [Get Chat ID for a Topic in a Group Chat](#get-chat-id-for-a-topic-in-a-group-chat)
1. [Edit Telegram Bot](#change-telegram-bot-avatar)
    1. [Change Telegram Bot Avatar](#change-telegram-bot-avatar)
    1. [Change Telegram Bot Name](#change-telegram-bot-name)
1. [Chat with Telegram Bot](#chat-with-telegram-bot)
    1. [Deploy a simple chat bot in Telegram](#chat-with-telegram-bot)
    1. [Use Telegram Bot to send a message](telegram_bot_send_message.ipynb)

## Create a Telegram Bot and get a Bot Token

1. Open Telegram application then search for `@BotFather`
1. Click Start
1. Click Menu -> /newbot or type `/newbot` and hit Send
1. Follow the instruction until we get message like so
    ```
    Done! Congratulations on your new bot. You will find it at t.me/new_bot.
    You can now add a description.....

    Use this token to access the HTTP API:
    63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c
    Keep your token secure and store it safely, it can be used by anyone to control your bot.

    For a description of the Bot API, see this page: https://core.telegram.org/bots/api
    ```
1. So here is our bot token `63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c` (make sure we don't share it to anyone).

[Back to top &uarr;](#how-to-start-with-telegram-bot-chat)

## Get Chat ID for a Private Chat

1. Search and open our new Telegram bot
1. Click Start or send a message
1. Open this URL in a browser `https://api.telegram.org/bot{our_bot_token}/getUpdates`   
    - See we need to prefix our token with a word `bot`
    - Eg: `https://api.telegram.org/bot81xxxxxx09:AAG-iOxxxxxxxxxxxWO-SBxxxxxxxxxxWg/getUpdates`
1. We will see a json like so
    ```
    {
      "ok": true,
      "result": [
        {
          "update_id": 83xxxxx35,
          "message": {
            "message_id": 2643,
            "from": {...},
            "chat": {
              "id": 29xxxxx08,           <-- chat_id
              "first_name": "...",
              "last_name": "...",
              "username": "@username",
              "type": "private"
            },
            "date": 1703062972,
            "text": "/start"
          }
        }
      ]
    }
    ```
1. Check the value of `result.0.message.chat.id`, and here is our Chat ID: `29xxxxx08`
3. Let's try to send a message: `https://api.telegram.org/bot81xxxxxx09:AAG-iOxxxxxxxxxxxWO-SBxxxxxxxxxxWg/sendMessage?chat_id=29xxxxx08&text=hello_world!`
4. When we set the bot token and chat id correctly, the message `hello_world!` should be arrived on our Telegram bot chat.

[Back to top &uarr;](#how-to-start-with-telegram-bot-chat)

## Get Chat ID for a Channel

1. Add our Telegram bot into a channel
1. Send a message to the channel
1. Open this URL `https://api.telegram.org/bot{our_bot_token}/getUpdates`
1. We will see a json like so
    ```
    {
      "ok": true,
      "result": [
        {
          "update_id": 838xxxx36,
          "channel_post": {...},
            "chat": {
              "id": -1001xxxxxx062,
              "title": "....",
              "type": "channel"
            },
            "date": 1703065989,
            "text": "test"
          }
      ]
    }
    ```
1. Check the value of `result.0.channel_post.chat.id`, and here is our Chat ID: `-1001xxxxxx062`
1. Let's try to send a message: `https://api.telegram.org/bot81xxxxxx09:AAG-iOxxxxxxxxxxxWO-SBxxxxxxxxxxWg/sendMessage?chat_id=-111xxxxxx200&text=hello_world~`
1. When we set the bot token and chat id correctly, the message `hello_world~` should be arrived on our Telegram channel.

[Back to top &uarr;](#how-to-start-with-telegram-bot-chat)

## Get Chat ID for a Group Chat

To get the chat ID of a Telegram group for your bot

1. Add our Telegram bot into a group
1. Send a message to the group
1. Open this URL `https://api.telegram.org/bot{our_bot_token}/getUpdates`
1. We will see a json like so
```
{
    "update_id": 8393,
    "message": {
        "message_id": 3,
        "from": {
            "id": 7474,
            "first_name": "Hiu"
        },
        "chat": {
            "id": -400xxxxxx10,       <-- group_chat_id
            "title": "Bot Alert"
        },
        "date": 25497,
        "new_chat_participant": {
            "id": 71, 
            "first_name": "Baechu",
            "username": "BeachuBot"
        }
    }
}
```
1. Check the value of `result.3.message.chat.id`, and here is our Chat ID: `-400xxxxxx10`
1. Let's try to send a message: `https://api.telegram.org/bot81xxxxxx09:AAG-iOxxxxxxxxxxxWO-SBxxxxxxxxxxWg/sendMessage?chat_id=-400xxxxxx10&text=hello_world~`
1. When we set the bot token and chat id correctly, the message `hello_world~` should be arrived on our Telegram channel.

[Back to top &uarr;](#how-to-start-with-telegram-bot-chat)

## Get Chat ID for a Topic in a Group Chat

In order to send a message to a specific topic on Telegram group, we need to get the topic ID.

1. Open Telegram in a desktop app
1. Add our Telegram bot into a chat group
1. Send a message to the chat group
1. Right click on the message and click `Copy Message Link`
    - We will get a link like so: `https://t.me/c/194xxxx987/11/13`
    - The pattern: `https://t.me/c/{group_chat_id}/{group_topic_id}/{message_id}`
    - So the group Topic ID is `11`.
1. Now we can use it like so (see `message_thread_id`): `https://api.telegram.org/bot783114779:AAEuRWDTFD2UQ7agBtFSuhJf2-NmvHN3OPc/sendMessage?chat_id=-100194xxxx987&message_thread_id=11&text=hello_world~`
1. When we set the bot token and chat id correctly, the message `hello_world~` should be arrived inside our group chat topic.
    
[Back to top &uarr;](#how-to-start-with-telegram-bot-chat)

## Change Telegram Bot Avatar

1. Go to the `@BotFather` bot and enter the `/setuserpic` command.
1. Select the bot that needs to change its avatar.
1. Send your desired avatar image.

[Back to top &uarr;](#how-to-start-with-telegram-bot-chat)

## Change Telegram Bot Name

1. Go to the `@BotFather` bot and enter the `/setname` command.
1. Select the bot you want to change the name of.
1. Write a new name and send.

[Back to top &uarr;](#how-to-start-with-telegram-bot-chat)

## Chat with Telegram Bot

1. Install `python-telegram-bot` package.
```
pip install python-telegram-bot
```
2. Create file [chat_with_bot.py](files/chat_with_bot.py)
3. Open Terminal and run the following command
```
python chat_with_bot.py
```
4. Open Telegram and send a message to your Bot.

5. Deploy the Bot 

[Back to top &uarr;](#how-to-start-with-telegram-bot-chat)

## Use Telegram Bot to send a message
See details in [telegram_bot_send_message](files/telegram_bot_send_message.ipynb)
