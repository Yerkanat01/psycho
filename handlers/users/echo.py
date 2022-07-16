from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(f'{message.chat.username},  {message.text}  бұл не? \n  Бастау үшін /start')
