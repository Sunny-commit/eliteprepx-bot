import telebot
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Import handlers
from handlers.start_handler import register_start_handler
from handlers.free_content_handler import register_free_handlers
from handlers.premium_handler import register_premium_handlers

# Register all
register_start_handler(bot)
register_free_handlers(bot)
register_premium_handlers(bot)

# Start polling
bot.infinity_polling()
