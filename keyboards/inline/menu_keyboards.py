from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu_cd = CallbackData("call","answer_id","previous_answer")

def make_callback_data(answer_id = 0,previous_answer= 0):
    return menu_cd.new(answer_id = answer_id,previous_answer = previous_answer)

async def answers_keyword(answer_data):
    answers,answers_id,previous_answer = answer_data

    markup = InlineKeyboardMarkup(row_width=1)
    if len(answers_id) == 1:
        for answer in answers:
            answer_id = answers_id[0]

            callback_data = make_callback_data(answer_id = answer_id,previous_answer=previous_answer)
            markup.insert(
                InlineKeyboardButton(
                    text=answer, callback_data=callback_data)
            )
    else:
        for answer,answer_id in zip(answers,answers_id):

            callback_data = make_callback_data(answer_id = answer_id,previous_answer=previous_answer)
            markup.insert(
                InlineKeyboardButton(
                    text=answer, callback_data=callback_data)
            )

    markup.row(
        InlineKeyboardButton(
            text="Басты бетке кайту",
            callback_data=make_callback_data(answer_id = 0,previous_answer=0)
        )
    )
    return markup

async def main_menu_keyboards():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.row(
        InlineKeyboardButton(
            text="Психологпен сырласу",
            callback_data='get_psycho'))
    markup.row(
        InlineKeyboardButton(
            text="Біз жайлы информация",
            callback_data="about_us"))
    markup.row(
        InlineKeyboardButton(
            text="8======D",
            callback_data='help'))

    return markup

