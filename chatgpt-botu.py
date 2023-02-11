import telegram
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Salam!")

def main():
    updater = Updater(token="1801568916:AAEToeCtmwjKkuU2mv9Eb9ff0xF9w4vUUvI", use_context=True)
    dp = updater.dispatcher
    start_handler = CommandHandler("start", start)
    dp.add_handler(start_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
