from django.conf import settings
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from congenial_bot.services import start, message


def run_bot():
    app = ApplicationBuilder().token(settings.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(~filters.COMMAND, message))
    app.run_polling()
