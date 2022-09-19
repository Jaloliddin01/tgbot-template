from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.answer("Bu nima rasm?")

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_handler(msg: types.Message):
    await msg.answer("Bu kim")

@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def voice_handler(msg: types.Message):
    await msg.answer("Tushunmadim?")

@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(msg: types.Message):
    await msg.answer("Bu qayer?")

@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def document_handler(msg: types.Message):
    await msg.answer("Bu qanaqa dokument?")

@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def sticker_handler(msg: types.Message):
    await msg.answer("😅")