import telegram
from telegram.ext import Updater, CommandHandler

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello")

# Set up the bot with your API token
updater = Updater("1801568916:AAEToeCtmwjKkuU2mv9Eb9ff0xF9w4vUUvI", use_context=True)

# Add a handler for the /start command
updater.dispatcher.add_handler(CommandHandler('start', start))

# Start the bot
updater.start_polling()
updater.idle()
