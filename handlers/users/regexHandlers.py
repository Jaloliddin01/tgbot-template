from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUMBER = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
COMMAND_EMAIL_REGEX = f"email:" + EMAIL_REGEX

@dp.message_handler(filters.Regexp(EMAIL_REGEX))
async def regex_email(message: types.Message):
    await message.answer('Email qabul qilindi')

@dp.message_handler(filters.Regexp(PHONE_NUMBER))
async def regex_phone(message: types.Message):
    await message.answer('Telefon raqam qabul qilindi')

@dp.message_handler(regexp_commands=[COMMAND_EMAIL_REGEX])
async def command_regex_email_example(message: types.Message):
    await message.answer('Email qabul qilindi')