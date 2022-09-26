import asyncio
from asgiref.sync import sync_to_async, async_to_sync

from django.conf import settings
from django.core.cache import cache
from telegram import Update, Bot
from telegram.ext import ContextTypes

from congenial_bot.models import Message


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cache.set("chat_id", update.effective_chat.id, 60 * 60 * 24)
    await update.message.reply_text(f"Start {update.effective_user.first_name}")


async def func():
    new_msg = Message()
    async_save = sync_to_async(new_msg.save)
    await async_save()


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Message {update.effective_user.first_name}")


async def send_message(chat_id: int, text: str):
    bot = Bot(settings.BOT_TOKEN)
    chat_id = cache.get("chat_id")
    await bot.send_message(chat_id=chat_id, text=text)


# async def func():
#     new_msg = Message()
#     async_save = sync_to_async(new_msg.save)
#     await async_save()
