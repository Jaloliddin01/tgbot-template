from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

@dp.message_handler(filters.Command('change_photo'), filters.AdminFilter())
async def changePhoto(message: types.Message):
    await message.answer('Rasmni almashtiramizmi?')
