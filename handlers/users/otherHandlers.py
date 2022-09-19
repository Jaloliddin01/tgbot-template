from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

@dp.message_handler(is_reply=True, commands='user_id')
async def reply_fltr(message: types.Message):
    await message.answer(message.reply_to_message.from_user.id)

@dp.message_handler(content_types='contact', is_sender_contact=True)
async def sender_contact(message: types.Message):
    await message.answer('Rahmat! Kontaktingiz qabul qilindi')

@dp.message_handler(is_forwarded=True)
async def froward_message(message: types.Message):
    await message.answer('Birovning xabarini menga yuboryapsizmi?')

@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands='shaxsiy')
async def chat_type(message: types.Message):
    await message.answer('Bu shaxsiy xabar')