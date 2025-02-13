from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes
import logging
import asyncio

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define the command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Play Game", url="https://baretap.github.io/blondieminigame/game.html")],
        [InlineKeyboardButton("View Wallet", url="https://baretap.github.io/blondieminigame/wallet.html")],
        [InlineKeyboardButton("View Tasks", url="https://baretap.github.io/blondieminigame/tasks.html")],
        [InlineKeyboardButton("Leaderboard", url="https://baretap.github.io/blondieminigame/leaderboard.html")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        'Welcome to the Blondie Mini Game! Click the buttons below to navigate:',
        reply_markup=reply_markup
    )
    await asyncio.sleep(1)

def main():
    application = Application.builder().token("7348594119:AAFkfxTpTbby1BP7GEUvuXgt5Ss9roKyeJk").build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()
