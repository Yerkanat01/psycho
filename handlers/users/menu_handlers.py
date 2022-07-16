import pandas as pd
from aiogram.types import CallbackQuery

from data.config import psycho_info_url
from loader import dp
from aiogram import types
from keyboards.inline.menu_keyboards import answers_keyword, menu_cd


async def answer(message: types.Message,data):
    question = data.question.values[0]
    previous_answer = data.previous_answer.values[0]
    answer_data = (str(data.answers.values[0]).split(','),str(data.answer_id.values[0]).split(','),previous_answer)
    data_url = data.data_url.values[0]
    data_type = data.data_type.values[0]
    if isinstance(message, types.Message):
        call = message
    elif isinstance(message, CallbackQuery):
        call = message.message
    answer_murkup = await answers_keyword(answer_data)
    media_func = {'photo':call.answer_photo(caption = question,photo = data_url, reply_markup = answer_murkup),
                  'text':call.answer(text = question, reply_markup = answer_murkup),
                  'audio':call.answer_audio(caption = question,audio = data_url, reply_markup = answer_murkup),
                  'video':call.answer(text = f'{question} \n{data_url}', reply_markup = answer_murkup),
                  'voice':call.answer_voice(caption = question,voice = data_url, reply_markup = answer_murkup),
                  }
    await media_func[data_type]


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    get_data = pd.read_csv("data - Лист1.csv")
    await call.message.edit_reply_markup()
    current_question = int(callback_data.get("answer_id"))
    if current_question < 3:
        await call.message.delete()

    datas = get_data.loc[get_data['previous_answer']==current_question]
    await answer(call, datas)

