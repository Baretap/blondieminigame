from telegram.ext import Updater, CommandHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the command handler
def start(update, context):
    update.message.reply_text('Welcome to the Blondie Mini Game! Click the Blondie image to score a point.')

def main():
    # Replace '' with your actual bot token
    updater = Updater("7348594119:AAFkfxTpTbby1BP7GEUvuXgt5Ss9roKyeJk", use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
