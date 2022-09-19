from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

SUPERUSER = [1843314238]
BLACKLIST = [1212121212]

@dp.message_handler(chat_id=SUPERUSER, text='secret')
async def id_filter_example(message: types.Message):
    await message.answer("Xush kelibsiz, SuperUser!")