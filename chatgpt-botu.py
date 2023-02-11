from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Salam!")

updater = Updater(token="1801568916:AAEToeCtmwjKkuU2mv9Eb9ff0xF9w4vUUvI", use_context=True)

start_handler = CommandHandler("start", start)
updater.dispatcher.add_handler(start_handler)

updater.start_polling()
