from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['rub', 'usd'])
async def hashtag_handler(message: types.Message):
    await message.answer('Akang kuchaydi uje!')