from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes
import logging
import asyncio

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Play", url="https://baretap.github.io/blondieminigame/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        'Tervetuloa Blondie Mini Gameen! Paina alla olevaa nappia aloittaaksesi pelin:',
        reply_markup=reply_markup
    )
    await asyncio.sleep(1)

def main():
    application = Application.builder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()
