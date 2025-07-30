from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Replace YOUR_BOT_TOKEN with your actual token
BOT_TOKEN = "81xxxxxx09:AAG-iOxxxxxxxxxxxWO-SBxxxxxxxxxxWg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command"""
    await update.message.reply_text("Happiness! Em là Irene-ssi. Anh cần em giúp gì ạ?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle messages from the user"""
    user_message = update.message.text.lower()
    
    greeting_words = ["hi","hello","chào"]
    farewell_words = ["bye", "bai", "bí bi"]

    if any(word in user_message for word in greeting_words):
        await update.message.reply_text("Hi anh~ 😊")

    elif any(word in user_message for word in farewell_words):
        await update.message.reply_text("Bye bye anh~ 👋🥹")
    else:
        await update.message.reply_text("Em xin lỗi. Em chưa hiểu ý của anh")

def main():
    """Run the bot"""
    # Create the application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Run the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()