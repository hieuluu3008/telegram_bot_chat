# 🚀 Getting Started with Telegram Bot Chat

This guide walks you through how to create, configure, and interact with a Telegram Bot. It includes steps for getting bot and chat IDs, changing bot settings, and sending messages.

---

## 1. 🔨 Create Bot
- Search `@BotFather` on Telegram
- Send `/newbot` → Get your **Bot Token**

## 2. 🆔 Get Chat IDs
- Use: `https://api.telegram.org/bot<token>/getUpdates`
- From response JSON:
  - `message.chat.id` → Private or Group
  - `channel_post.chat.id` → Channel
  - `message_thread_id` → Group Topic

## 3. ✏️ Customize Bot
- `/setuserpic` → Change avatar
- `/setname` → Change name

## 4. 💬 Send Messages
- API format:
  ```
  https://api.telegram.org/bot<token>/sendMessage?chat_id=<id>&text=hello
  ```

## 5. 🐍 Python Bot (Optional)
1. Install: `pip install python-telegram-bot`
2. Run your bot script
