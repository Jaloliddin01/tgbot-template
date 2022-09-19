from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp

@dp.message_handler(Text(contains=['yaxshimisiz', 'assalom'], ignore_case=True))
async def text_example(message: types.Message):
    await message.reply("Va alaykum assalom. Yaxshi, o'zingiz yaxshimi?")

@dp.message_handler(Text(contains='assalom', ignore_case=True))
@dp.message_handler(Text(equals='assalom alaykum', ignore_case=True))
async def text_example(message: types.Message):
    await message.reply('Waalaykum assalom')

@dp.message_handler(Text(contains='yaxshimisiz', ignore_case=True))
async def text_example(message: types.Message):
    await message.reply("Yaxshi, o'zingiz yaxshimi?")
