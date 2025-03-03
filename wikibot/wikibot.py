import asyncio
import logging
import sys
import wikipedia
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "5365270553:AAGKy7ofpBtoI-eSH2xCrZcf6cnv7gDFRiE"
wikipedia.set_lang('uz')
# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"<b>Assalomu alaykum!</b>\n<em>Wikipedia Botiga Xush kelibsiz!</em>, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def sendwiki(message: Message):
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        respond=wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Bu mavzuga oid maqola topilmadi!!!")


async def main():
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())