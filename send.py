import asyncio
import os

from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def send_message(chat_id: int, text: str) -> None:
    bot = Bot(BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text=text)

if __name__ == "__main__":
    asyncio.run(send_message(chat_id=1242849836, text="Test notification"))