import pandas as pd
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import psycho_info_url, admins
from handlers.users.menu_handlers import answer
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    get_data = pd.read_csv("data - Лист1.csv")
    await message.delete()
    datas = get_data.loc[get_data['previous_answer']==0]
    await answer(message,datas)



